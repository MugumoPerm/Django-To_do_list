from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django import forms

tasks = ["cook"]

# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="New Task")


# Create your views here.
def tasks(request):
    return render(request, "tasks.html", {
        "task_list": tasks
    })

def add(request):
    return render(request, "add.html")