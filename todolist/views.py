from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import SignUpForm

# Create your views here.

def test(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'auth_base.html')


def todo_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return render(request, 'login.html')


def todo_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')

def todo_signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'signup_form': signup_form})
