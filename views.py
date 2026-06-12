from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# 1. View All Tasks & Create Task
def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('task_list')
        
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# 2. Mark Task as Completed
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('task_list')

# 3. Delete Task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')