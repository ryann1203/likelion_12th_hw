from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import Http404

from .models import Post, Comment, Tag
# Create your views here.

def mainpage(request):
    context = {
        'generation': 12,
        'members': ['현아', '영심이', '티준'],
        'info':{'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'},
        'sessions':['장고는 MTV 패턴을 기반으로 한 프레임워크이다.', 'MTV 패턴에는 Model, Template, View가 있다.',
                   'Model은 데이터, View는 요청에 따른 적절한 로직 수행, Template은 인터페이스를 의미한다.']
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    posts = Post.objects.all()
    return render(request, 'main/secondpage.html', {'posts' : posts})

def new_post(request):
    return render(request, 'main/new-post.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post' : post, 'comments' : comments})
    
    elif request.method == 'POST':
        new_comment = Comment()

        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()
        new_comment.save()
        words = new_comment.content.split(' ')
        tag_list = []

        for w in words:
            if len(w) > 0:
                if w[0] == '#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_comment.tags.add(tag.id)

        # new_comment.save()s
        return redirect('main:detail', id)

def edit(request, id):
    edit_post = Post.objects.get(pk = id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def create(request):
    if request.user.is_authenticated:
        new_post = Post()

        new_post.title = request.POST['title']
        new_post.weather = request.POST['weather']
        new_post.writer = request.user
        new_post.body = request.POST['body']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')

        new_post.save()

        words = new_post.body.split(' ')
        tag_list = []

        for w in words:
            if len(w) > 0:
                if w[0] == '#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)

        return redirect('main:detail', new_post.id)
    
    else:
        return redirect('accounts:login')

def update(request, id):
    update_post = Post.objects.get(pk=id)

    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.weather = request.POST['weather']
        # update_post.writer = request.POST['writer']
        update_post.body = request.POST['body']
        update_post.pub_date = timezone.now()

        words = update_post.body.split(' ')
        tag_list = []

        for w in words:
            if len(w) > 0:
                if w[0] == '#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            update_post.tags.add(tag.id)

        if request.FILES.get('image'):
            update_post.image = request.FILES['image']

        update_post.save()
        return redirect('main:detail', update_post.id)
    return redirect('accounts:login', update_post.id)

def delete(request, id):
    try:
        # 먼저 Comment 객체를 시도
        comment = Comment.objects.get(pk=id)
        if request.user.is_authenticated and request.user == comment.writer:
            post_id = comment.post.id
            comment.delete()
            return redirect('main:detail', post_id)
    except Comment.DoesNotExist:
        # Comment 객체가 없으면 Post 객체 시도
        try:
            post = Post.objects.get(pk=id)
            if request.user.is_authenticated and request.user == post.writer:
                post.delete()
                return redirect('main:secondpage')
        except Post.DoesNotExist:
            raise Http404("삭제할 객체가 없습니다.")

    raise Http404("접근 권한이 없습니다.")

    
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags' : tags})

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    comments = tag.comments.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts,
        'comments' : comments
    })

def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post.id)
