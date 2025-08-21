from django.shortcuts import render
from todo.models import Task
def home(request):
    task_list = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completed_task_list = Task.objects.filter(is_completed=True)
    context = {
        "tasks": task_list,
        "completed_task": completed_task_list
    }
    return render(request, 'home.html', context)
