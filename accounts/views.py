from django.shortcuts import render
from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
# Create your views here.
def register(request):
    if request.method == 'POST':
        fname=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if(User.objects.filter(email=email).exists()):
            messages.info(request,'email exists ')
            return redirect('register')
        else:
            user=User.objects.create_user(password=password,first_name=fname,email=email,username=fname)
            user.save()
            print('user created')
            return redirect('login')

    else:
        return render(request,'register.html')

def login(request):
    if request.method =='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        print(uname)
        print(password)
        user=auth.authenticate(username=uname,password=password)
        print("welcome11")
        print(user)
        if(user is not None):
            auth.login(request,user)
            print("welcome")
            return redirect('dashboard/dashboard')
        else:
            messages.info(request,"invalid credentials")
            print("invalid")
            return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')