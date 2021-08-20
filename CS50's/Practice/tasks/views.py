from django.shortcuts import render,redirect
from .models import Task

tasks = Task.objects.all()
# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{"tasks":tasks})
def add(request):
    if request.method == 'POST':
        new_item = request.POST["task"]
        new_task=Task.objects.create(Title=new_item)
        new_task.save()
        return redirect('tasks:index')
    else:
        return render(request,"tasks/add.html")
# def add(request):
#     if request.method == 'POST':
#         new_item = request.POST['task']
#         new_task=Task.objects.create(Title=new_item)
#         new_task.save()

#         return redirect('tasks:index')

#     else:
#         return render(request,"tasks/add.html")
