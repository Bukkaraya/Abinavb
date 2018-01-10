from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context_dict = {'active': 'home'}
    return render(request, 'bukkaraya/index.html', context_dict)
