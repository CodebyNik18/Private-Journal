from django.shortcuts import render, redirect
from .models import AddJournal


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        AddJournal.objects.create(title=title, content=content, user=request.user)
        return redirect('journals_notes')
    return render(request=request, template_name='add_journal.html')


def edit_journal(request, pk):
    journal = AddJournal.objects.get(user=request.user, pk=pk)
    if request.method == 'POST':
        title_new = request.POST['title']
        content_new = request.POST['content']
        
        journal.title = title_new
        journal.content = content_new
        journal.save()
        return redirect('journals_notes')
        
    context = {
        'journal': journal
    }
    return render(request=request, template_name='edit_journal.html', context=context)