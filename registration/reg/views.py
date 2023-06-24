from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method== 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return redirect('signup')
        my_user = User.objects.create(username=uname, email=email, password=pass1)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.post.get('username')
        password=request.post.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
