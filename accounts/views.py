from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdate(request.POST, request.FILES, instance=request.user.userdetail)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdate(instance=request.user.userdetail)
    return render(request, 'profile.html', {'uform':uform, 'pform':pform})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts:posts')

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
    return redirect('auth:login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('posts:posts')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})