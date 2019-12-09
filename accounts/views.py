from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def accounts_view(request):
    return render(request,'accounts/accountspage.html')

def signup_view(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username']) 
                return render(request,'accounts/signuppage.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])        
                auth.login(request,user)
                return redirect('homepage')
        else:
            return render(request,'accounts/signuppage.html', {'error':'Password didnot match!'})
    else: 
        return render(request,"accounts/signuppage.html")

def login_view(request):
    return render(request,"accounts/loginpage.html")

def logout_view(request):
    # todo need to route to homepage and donot forget to logout.
    return render(request,"accounts/signuppage.html")