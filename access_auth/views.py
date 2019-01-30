
# Django 
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Forms
from access_auth.forms import LoginForm, registerForm

@login_required()
def home(request):
    return render(request, 'pages/home.html')

def login_v(request):

    if request.method == 'POST':
    
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            
            email = request.POST['email']
            password = request.POST['password']
            
            # Continue login..
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('access_auth:home')
            else:
                return render(request, 'pages/login.html', {'message' : 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'pages/login.html', {'form': form})
    return render(request, 'pages/login.html')

def signup_v(request):

    if request.method == 'POST':

        form = registerForm(request.POST)
        if form.is_valid():
            return redirect('access_auth:login')
        else:
            return render(request, 'pages/signup.html', { 'form' : form})

    return render(request, 'pages/signup.html')