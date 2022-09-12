from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users
from products.models import Order
from django.contrib.auth.models import User

@login_required(login_url="login")
@allowed_users(roles=["user"])
def user_page(request):
    user = User.objects.get(id=request.user.id)
    orders = user.customer.order_set
    total_orders = orders.all().count()
    delivered_orders = orders.filter(status="Delivered").count()
    pending_orders = orders.filter(status="Pending").count()

    orders = orders.all()

    context = {
        "total_orders": total_orders,
        "delivered_orders": delivered_orders,
        "pending_orders": pending_orders,
        "orders": orders
    }
    return render(request, "users/user_page.html", context)

def user_settings(request):
    
    context = {}
    return render(request, "users/user_settings.html", context)