
# Django 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Forms
from access_auth.forms import LoginForm, registerForm

# Utils
from utils.responses import sendResponse, sendError

def getUserInfo(request):
    """Return the user's basic information to use in frontend"""
    
    if not request.user.is_anonymous:

        data = {
            'id': request.user.id,
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }

        if hasattr(request.user, 'teacher'):
            data['type'] = 'teacher'
        else:
            data['type'] = 'student'
 
        return sendResponse(data, 'Usuario logeado')
    else:
        return sendError('Debes estar logeado', 401)

@login_required()
def home(request):
    if(request.user.teacher):
        return redirect('/maestros')
    else:
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
                if user.teacher:
                    return redirect('http://localhost:8080/maestros/grupos')
                elif user.student:
                    return redirect('http://localhost:8080/estudiantes')
            else:
                return render(request, 'pages/login.html', {'message' : 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'pages/login.html', {'form': form})
    return render(request, 'pages/login.html')

def signup_v(request):

    if request.method == 'POST':

        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access_auth:login')
        else:
            return render(request, 'pages/signup.html', { 'form' : form})

    return render(request, 'pages/signup.html')

def logout_v(request):
    logout(request)
    return redirect('access_auth:home')