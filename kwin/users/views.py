from django.shortcuts import render

# Create your views here.
def user_register(request):
    context = {}
    return render(request, 'users/register.html', context)

def user_login(request):
    context = {}
    return render(request, 'users/login.html', context)


