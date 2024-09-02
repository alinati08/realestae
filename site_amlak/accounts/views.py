from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

# Create your views here.

def login(request):
    if request.method == "POST":
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            # messages.info(request,'Invalid credentials')
            messages.info(request," نام کاربری یا رمز عبور اشتباه است ")
            return redirect('login')

    else:
        return render(request, 'registration/login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        username = request.POST['username']
        if password == c_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'این نام کاربری قبلا ایجاد شده است ')
                return redirect('signup')
                # for printing on console
                # print('Username taken')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'این ایمیل قبلا استفاده شده است ')
                return redirect('signup')
                #print('Email taken')
            else:
                user =  User.objects.create_user(username = username, password = c_password, email=email, first_name = first_name, last_name= last_name)
                user.save()
                messages.info(request,'ثبت نام شما کامل شد ')
                return redirect('login')
        else:
            messages.info(request,'تکرار رمز عبور با رمز عبور باید یکسان باشد ')
            return redirect('signup')
    else:
        return render(request,'registration/signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')