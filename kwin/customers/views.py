from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = customer.order_set.count()

    context = {
        "customer": customer,
        "orders": orders,
        "total_order": total_order
    }
    return render(request, 'customers/customer_details.html', context)

def create_customer(request):
    context = {}
    return render(request, 'customers/create_customer.html', context)