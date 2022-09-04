from django.urls import path
from . import views

urlpatterns = [
    path('customer_details/<int:pk>', views.customer, name="customer_details"),
    path('create_customer', views.create_customer, name="create_customer"),
    path('update_customer/<int:pk>', views.update_customer, name="update_customer"),
    path('delete_customer/<int:pk>', views.delete_customer, name="delete_customer")
]