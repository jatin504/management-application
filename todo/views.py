from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from todo.models import Task
# Create your views here.

def addTask(req):
    task = req.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')