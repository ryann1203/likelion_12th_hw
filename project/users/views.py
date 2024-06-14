from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Post

# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    followers = user.profile.followers.all()
    followings = user.profile.followings.all()
    context = {
        'user' : user,
        'followers': followers,
        'followings': followings
    }
    return render(request, 'users/mypage.html', context)

    # all_posts = Post.objects.all()
    # user_posts = []

    # # 현재 로그인한 사용자가 작성한 게시글만 user_posts에 추가
    # for post in all_posts:
    #     if post.writer == request.user.username:
    #         user_posts.append(post)

    # return render(request, 'users/mypage.html', {'posts': user_posts})


def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)

    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)