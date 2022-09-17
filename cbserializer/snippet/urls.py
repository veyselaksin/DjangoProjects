from django.urls import path
from . import views

urlpatterns = [
    path('snippets-list/', views.SnippetList.as_view(), name="snippets-list"),
    path('snippets-detail/<str:pk>', views.SnippetDetails.as_view(), name="snippets-detail"),
]

