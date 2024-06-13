from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

from main.models import Post

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
        
        else:
            return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == 'POST':

        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )

            club=request.POST['club']
            grade=request.POST['grade']

            profile = Profile(user=user, club=club, grade=grade)
            profile.save()

            auth.login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/signup.html')
    

# def mypage(request):
#     all_posts = Post.objects.all()
#     user_posts = []

#     # 현재 로그인한 사용자가 작성한 게시글만 user_posts에 추가
#     for post in all_posts:
#         if post.writer == request.user.username:
#             user_posts.append(post)

#     return render(request, 'users/mypage.html', {'posts': user_posts})