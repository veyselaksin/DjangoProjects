from django.shortcuts import render, redirect
from .models import CreateUserForm
from django.contrib import messages

# Create your views here.
def user_register(request):
    registerForm = CreateUserForm()

    if request.method == "POST":
        registerForm = CreateUserForm(request.POST)
        print(registerForm.errors)
        if registerForm.is_valid():
            registerForm.save()
            username = registerForm.cleaned_data.get("username")
            messages.success(request, 'Account was created for ' + username)
            return redirect("login")
            
    context = {
        "register_form": registerForm
    }
    return render(request, 'pages/register.html', context)

def user_login(request):
    context = {}
    return render(request, 'pages/login.html', context)



