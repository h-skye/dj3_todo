from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'todo/home.html')
# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        # Creates a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos') #needs to be imported from shortcuts
            except IntegrityError: # A user already exists
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})

        else:
            # Tell the user the passwords didn't match
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')