from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

task = ["cook"]


# Create your views here.
def tasks(request):
    return render(request, "tasks.html", {
        "task_list": task
    })

def add(request):
    return render(request, "add.html")