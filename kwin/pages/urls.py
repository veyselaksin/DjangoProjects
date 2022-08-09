from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products', views.products, name="products"),
    path('customers', views.customers, name="customers")
]