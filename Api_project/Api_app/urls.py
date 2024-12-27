# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_htmmllist, name='item_htmllist'),
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/<int:pk>/', views.item_delete, name='item_delete'),
]
