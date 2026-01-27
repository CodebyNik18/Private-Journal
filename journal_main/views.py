from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.models import User
from journals.models import AddJournal

def home(request):
    return render(request=request, template_name='home.html')

def journals(request):
    _journals = AddJournal.objects.filter(user=request.user)
    context = {
        'journals': _journals,
    }
    return render(request=request, template_name='journal.html', context=context)