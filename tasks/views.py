from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def tasks(request):
    return render(request, "tasks.html")

def add(request):
    return render(request, "add.html")