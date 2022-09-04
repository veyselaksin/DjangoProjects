from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Customer
from products.filters import OrderFilter
from .forms import CustomerForm

# Create your views here.
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = customer.order_set.count()

    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders = orderFilter.qs

    context = {
        "customer": customer,
        "orders": orders,
        "total_order": total_order,
        "order_filter": orderFilter
    }
    return render(request, 'customers/customer_details.html', context)

def create_customer(request):
    customerForm = CustomerForm()

    if request.method == 'POST':
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid():
            customerForm.save()
            return redirect("/")
    context = {
        "customer_form": customerForm
    }
    return render(request, 'customers/create_customer.html', context)

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)

    customerForm = CustomerForm(instance=customer)

    if request.method == 'POST':
        customerForm = CustomerForm(request.POST, instance=customer)
        if customerForm.is_valid():
            customerForm.save()
            return redirect("customer_details", customer.id)

    context = {
        "customer_form": customerForm
    }
    return render(request, 'customers/update_customer.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect("/")
    
    context = {
        "customer": customer
    }
    return render(request, 'customers/delete_customer.html', context)