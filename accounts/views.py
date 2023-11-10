from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts:posts')  # Redirect to a different page if already logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:posts')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('auth:login')  # Redirect to the login page after logout



def register_view(request):
    if request.user.is_authenticated:
        return redirect('posts:posts')  # Redirect to a different page if already logged in

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})