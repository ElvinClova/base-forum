from ast import Delete
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('delete/<int:post_id>/', views.delete, name = 'delete'),
]