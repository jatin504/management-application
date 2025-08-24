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

def mark_as_un_done(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(req, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if req.method == 'POST':
        new_task = req.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            "get_task": get_task
        }
        return render(req, 'edit.html', context)

def delete_task(req, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()

    return redirect('home')