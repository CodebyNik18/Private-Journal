from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.models import User

def home(request):
    return render(request=request, template_name='home.html')

def journals(request):
    return render(request=request, template_name='journal.html')