from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context_dict = {'active': 'home'}
    return render(request, 'bukkaraya/index.html', context_dict)

def projects(request):
    context_dict = {'active': 'projects'}
    return render(request, 'bukkaraya/projects.html', context_dict)

def contact(request):
    context_dict = {'active': 'contact'}
    return render(request, 'bukkaraya/contact.html', context_dict)