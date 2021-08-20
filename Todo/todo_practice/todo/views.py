from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http.response import HttpResponseRedirect

# Create your views here.

class NewtaskForm(forms.Form):
    task = forms.CharField(label="add task")
    time = forms.IntegerField(max_value=12)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] =[]
        request.session["time"] =[]
    return render(request,"todo/index.html",{
        "tasks":request.session["tasks"],
        "time":request.session["time"]
    })

def add(request):
    if request.method== "POST":
        form  = NewtaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            time=form.cleaned_data["time"]
            request.session["tasks"] += [task]
            request.session["time"] +=[time]
            return HttpResponseRedirect(reverse("todo_list:index"))
        else:
            return render(request,'todo/add.html',{
                "form":form
            })
    return render(request,"todo/add.html",{
        "form":NewtaskForm()
    })
