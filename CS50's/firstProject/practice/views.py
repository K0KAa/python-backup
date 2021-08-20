from django.db.models.base import Model
from .models import Task
from django.shortcuts import redirect, render

tasks = Task.objects.all()
# Create your views here.
def index(request):
    return render(request,"practice/index.html",{"tasks":tasks})

def add(request):
    if request.method == 'POST':
        new_item = request.POST["task"]
        new_task = tasks.Title.create(Title =new_item)
        new_task.save()
        return redirect("practice:index")
    else:
        return render(request,"practice/index.html")
