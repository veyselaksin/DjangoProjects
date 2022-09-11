from django.shortcuts import render, redirect
from .models import Product, Order
from customers.models import Customer
from .forms import OrderForm
from django import forms
from django.contrib.auth.decorators import login_required 
from authentication.decorators import allowed_users
# Create your views here.

@login_required(login_url="login")
@allowed_users(roles=["admin", "customer", "user"])
def products(request):
    products = Product.objects.all()

    context = {
       "products": products 
    }
    return render(request, 'products/products.html', context)

@login_required(login_url="login")
@allowed_users(roles=["admin"])
def create_order(request, pk):
   customer = Customer.objects.get(id=pk)
   order_form = OrderForm(initial={"customer":customer})
   # order_form.fields["customer"].widget = order_form.hidden_fields()
   order_form.fields["customer"].widget = forms.HiddenInput()

   if request.method == 'POST':
      order_form = OrderForm(request.POST)
      if order_form.is_valid():
         order_form.save()
         return redirect('customer_details', customer.id)

   # print(order_form.fields["customer"].bound_data(data=customer, initial=None))

   context = {
      'order_form': order_form
   }
   return render(request, 'products/create_order.html', context)

@login_required(login_url="login")
@allowed_users(roles=["admin"])
def update_order(request, pk):
   order = Order.objects.get(id=pk)
   order_form = OrderForm(instance=order)

   if request.method == 'POST':
      order_form = OrderForm(request.POST, instance=order)
      if order_form.is_valid():
         order_form.save()
         return redirect('/')

   context = {
      'order_form': order_form
   }
   return render(request, 'products/update_order.html', context)

@login_required(login_url="login")
@allowed_users(roles=["admin"])
def delete_order(request, pk):
   order = Order.objects.get(id=pk)

   if request.method == 'POST':
      order.delete()
      return redirect('/')

   context = {
      'order': order
   }
   return render(request, 'products/delete_order.html', context)