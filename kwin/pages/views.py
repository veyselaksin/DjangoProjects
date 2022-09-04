from django.shortcuts import render
from . import helper
from customers.models import Customer
from products.models import Order

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = Order.objects.all().count()
    delivered_orders = Order.objects.filter(status="Delivered").count()
    pending_orders = Order.objects.filter(status="Pending").count()

    context = {
        "customers": customers,
        "orders": orders,
        "total_orders": total_orders,
        "delivered_orders": delivered_orders,
        "pending_orders": pending_orders
    }
    return render(request, 'pages/home.html', context)
