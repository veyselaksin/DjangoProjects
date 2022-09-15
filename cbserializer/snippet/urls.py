from django.urls import path
from . import views

urlpatterns = [
    path('snippets-list/', views.snippet_list, name="snippets-list"),
    path('snippets-detail/<str:pk>', views.snippet_detail, name="snippets-detail"),
]

