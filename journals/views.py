from django.shortcuts import render


def add(request):
    return render(request=request, template_name='add_journal.html')