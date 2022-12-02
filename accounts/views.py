from django.shortcuts import render , redirect
from accounts.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        nickname = request.POST['nickname']
        email = request.POST['email']
        if password == password2:
            
            user = User.objects.create_user(
                username=username,
                password=password,
                nickname=nickname,
                email=email
            )
            user.save()
            return redirect('/accounts/login')
        else:
            context = {'error': '비밀번호가 서로 일치하지 않습니다.'}
            return render(request, 'signup.html',context)
    else:
        return render(request,'signup.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request,username= username, password=password)
        if user is not None : 
            auth.login(request, user)
            return redirect('/')
        else : 
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')
    
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('/accounts/login')

