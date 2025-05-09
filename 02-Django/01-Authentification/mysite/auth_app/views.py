from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('auth_app:home')
        else:
            messages.success(request, "error")
            return redirect('auth_app:login')

    return render(request, 'authentification/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('auth_app:login')


def home(request):
    return render(request, "authentification/home.html", {})
