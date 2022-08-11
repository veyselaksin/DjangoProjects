from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm

# Create your views here.
def products(request):
    products = Product.objects.all()

    context = {
       "products": products 
    }
    return render(request, 'products/products.html', context)

def create_order(request):
   order_form = OrderForm()

   if request.method == 'POST':
      order_form = OrderForm(request.POST)
      if order_form.is_valid():
         order_form.save()
         return redirect('/')

   context = {
      'order_form': order_form
   }
   return render(request, 'products/create_order.html', context)

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

def delete_order(request, pk):
   order = Order.objects.get(id=pk)

   if request.method == 'POST':
      order.delete()
      return redirect('/')

   context = {
      'order': order
   }
   return render(request, 'products/delete_order.html', context)