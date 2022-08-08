from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name="task_list"),
    path('task/<int:pk>', views.TaskDetail.as_view(), name="task_detail"),
    path('task_create/', views.TaskCreate.as_view(), name="task_create"),
    path('task_update/<int:pk>/', views.TaskUpdate.as_view(), name="task_update"),
    path('task_delete/<int:pk>/', views.TaskDelete.as_view(), name="task_delete")
]