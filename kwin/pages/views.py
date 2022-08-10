from django.shortcuts import render
from . import helper
from customers.models import Customer
from products.models import Order

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    context = {
        "customers": customers,
        "orders": orders
    }
    return render(request, 'pages/home.html', context)
