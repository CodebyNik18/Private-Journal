from django.shortcuts import render, redirect
from django.urls import include
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def sign_in(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(name, email, password)
        
        messages.success(request, "Account created successfully. You can now log in.")
        
        return redirect('log_in')
    return render(request=request, template_name='sign_up.html')



def log_in(request):
    
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=name, password=password)
        
        if user:
            login(request=request, user=user)
            return redirect('journals_notes')
        else:
            messages.error(request, 'Invalid username or password..')
            
    return render(request=request, template_name='login.html')

def about(request):
    return render(request=request, template_name='about.html')