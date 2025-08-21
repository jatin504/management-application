from django.shortcuts import render
from todo.models import Task
def home(request):
    task_list = Task.objects.filter(is_completed=False)
    context = {
        "tasks": task_list
    }
    return render(request, 'home.html', context)
