from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


def sign_in(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(name, email, password)
        
        messages.success(request, "Account created successfully. You can now log in.")
        
        return redirect('login')
    return render(request=request, template_name='sign_up.html')

def login(request):
    return render(request=request, template_name='login.html')

def about(request):
    return render(request=request, template_name='about.html')