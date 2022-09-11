from tokenize import group
from django.shortcuts import render, redirect

from customers.models import Customer

from .decorators import unauthenticate_user
from .models import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

# Create your views here.
@unauthenticate_user
def user_register(request):
    registerForm = CreateUserForm()

    if request.method == "POST":
        registerForm = CreateUserForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()
            username = registerForm.cleaned_data.get("username")

            group = Group.objects.get(name="user")
            user.groups.add(group)

            Customer.objects.create(
                user=User.objects.get(id=user.id),
                name=User.objects.get(id=user.id).first_name,
                email=User.objects.get(id=user.id).email,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect("login")
            
    context = {
        "register_form": registerForm
    }
    return render(request, 'pages/register.html', context)

@unauthenticate_user
def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect("home")
        messages.error(request, 'Incorrect username or password!')
    context = {}
    return render(request, 'pages/login.html', context)

def user_logout(request):
    logout(request)
    return redirect("login")


