from django.urls import path, include
from . import views

urlpatterns = [
    path('snippets-list/', views.SnippetList.as_view(), name="snippets-list"),
    path('snippets-detail/<str:pk>', views.SnippetDetails.as_view(), name="snippets-detail"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]