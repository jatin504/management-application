from django.shortcuts import render, HttpResponse, redirect
from todo.models import Task
# Create your views here.

def addTask(req):
    task = req.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
