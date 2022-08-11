from django.urls import path
from . import views

urlpatterns = [
    path('customer_details/<int:pk>', views.customer, name="customer_details")
]