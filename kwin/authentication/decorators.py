from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticate_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            groups = None
            if request.user.groups.exists():
                groups = request.user.groups.all()
            
            if groups == None:
                return HttpResponse("You haven't got a group!")

            for group in groups:
                if group.name in roles:
                    return view_func(request, *args, **kwargs)
            return HttpResponse("You are not authorized to view this page!")
        return wrapper
    return decorator

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        groups = None
        if request.user.groups.exists():
            groups = request.user.groups.all()

            for group in groups:
                if group.name == "admin":
                    return view_func(request, *args, **kwargs)

                if group.name != "admin":
                    return redirect("user_page")
    return wrapper