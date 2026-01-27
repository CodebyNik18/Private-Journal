from django.shortcuts import render, redirect
from .models import AddJournal


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        AddJournal.objects.create(title=title, content=content, user=request.user)
        return redirect('journals_notes')
    return render(request=request, template_name='add_journal.html')