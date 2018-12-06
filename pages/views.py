
# Django 
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def login_v(request):

    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)[0]

        if user is not None:
            # Continue login..
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                return render(request, 'pages/login.html', {'message' : 'Usuario o contraseña incorrectos'})
                

    return render(request, 'pages/login.html')