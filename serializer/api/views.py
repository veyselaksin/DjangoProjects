from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Details': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'

    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    taskSerializer = TaskSerializer(tasks, many=True)
    return Response(taskSerializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    taskSerializer = TaskSerializer(task, many=False)
    return Response(taskSerializer.data)

@api_view(['GET','POST'])
def task_create(request):
    taskSerializer = TaskSerializer(data=request.data)
    if taskSerializer.is_valid():
        taskSerializer.save()
    return Response(taskSerializer.data)

@api_view(['GET', 'PUT'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    taskSerializer = TaskSerializer(instance=task, data=request.data)

    if taskSerializer.is_valid():
        taskSerializer.save()
    return Response(taskSerializer.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item successfuly deleted!")