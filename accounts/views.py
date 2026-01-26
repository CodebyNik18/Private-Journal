from django.shortcuts import render
from django.http import HttpResponse


def sign_in(request):
    return render(request=request, template_name='sign_up.html')

def login(request):
    return render(request=request, template_name='login.html')

def about(request):
    return render(request=request, template_name='about.html')