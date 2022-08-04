from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task
from typing import Optional
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name: str = 'tasks/tasks.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name: Optional[str] = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')