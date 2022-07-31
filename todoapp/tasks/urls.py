from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name="tasks"),
    path('update_task/<str:pk>', views.update_task, name="update_task"),
    path('delete_task/<int:pk>', views.delete_task, name="delete_task")
]
