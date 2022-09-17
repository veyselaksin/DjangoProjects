from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request):
        snippet = Snippet.objects.all()
        snippetSerializer = SnippetSerializer(data=snippet, many=True)
        if snippetSerializer.is_valid():
            return Response(snippetSerializer.data) 
        return Response(snippetSerializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetails(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    @csrf_exempt
    def get_object(self, pk):

        try:
            self.snippet = Snippet.objects.get(id=pk)
        except:
            return Response("Data not found!", status=status.HTTP_400_BAD_REQUEST)

    def get(self):
        serializer = SnippetSerializer(self.snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self):
        data = JSONParser().parse(self.request)
        serializer = SnippetSerializer(self.snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self):
        self.snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        