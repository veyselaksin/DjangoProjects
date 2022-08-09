from django.shortcuts import render
from . import helper

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def products(request):
    return render(request, 'pages/products.html')

def customers(request):
    return render(request, 'pages/customers.html')