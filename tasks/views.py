from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django import forms



class NewTaskForm(forms.Form):
    task = forms.CharField()


# Create your views here.
def tasks(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
   if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks"))
        else:
            return render(request, "add.html",{
                "form": form
            })
   else:   
        return render(request, "add.html", {
            "form": NewTaskForm()
        })