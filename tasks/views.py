from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django import forms

tasked = ["cook"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def tasks(request):
    return render(request, "tasks.html", {
        "tasked": tasked
    })

def add(request):
   if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasked.append(task)
            return HttpResponseRedirect(reverse("tasks"))
        else:
            return render(request, "add.html",{
                "form": form
            })
   else:   
        return render(request, "add.html", {
            "form": NewTaskForm()
        })