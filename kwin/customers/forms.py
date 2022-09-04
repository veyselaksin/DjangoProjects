from django.forms import ModelForm
from .models import Customer
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widget = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"})
        }