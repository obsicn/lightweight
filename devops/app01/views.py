from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    message = 'Hello world from Michael'
    print(message)
    return HttpResponse(message)