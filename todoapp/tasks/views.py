from django.shortcuts import redirect, render
from .models import Task
from .froms import TaskForm

# Create your views here.
def tasks(request): 
    all_task = Task.objects.all()

    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task_form.save()
        return redirect("/tasks")

    context = {
        'tasks': all_task,
        'task_form': task_form
    }
    return render(request, 'tasks/tasks.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)

    task_form = TaskForm(instance=task)

    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)

        if task_form.is_valid():
            task_form.save()
        return redirect("/tasks")
    
    context = {
        "task_form": task_form
    }

    return render(request, "tasks/update_task.html", context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/tasks")
    
    context = {
        "task": task
    }
    return render(request, "tasks/delete_task.html", context)
