from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

class NewtaskForm(forms.Form):
    task = forms.CharField(label="new task")
    # priority = forms.IntegerField(label="Priority",min_value=1,max_value=10)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] =[]
    return render(request, "hello/index.html",{
        "tasks":request.session["tasks"]
    })

def kushal(request):
    return HttpResponse("Fuck off")

def david(request):
    return HttpResponse("hello david")


def greets(request,name):
    return render(request, "hello/greet.html",{
        "name":name.capitalize()
    })

def add(request):
    if request.method=="POST":
        form= NewtaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+= [task]
            return HttpResponseRedirect(reverse("hello:index"))
        else:
            return render(request,"hello/add.html",{
                "form":form
            })
    return render(request,'hello/add.html',{
        "form":NewtaskForm()
    })