from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == "GET":
        snippet = Snippet.objects.all()
        snippetSerializer = SnippetSerializer(data=snippet, many=True)
        if snippetSerializer.is_valid():
            return JsonResponse(snippetSerializer.data, safe=False) 

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
    return JsonResponse(snippetSerializer.data, safe=False, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        snippet = Snippet.objects.get(id=pk)
    except:
        return HttpResponse("Data not found!", status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204) 
    
    return JsonResponse(serializer.data, safe=False)