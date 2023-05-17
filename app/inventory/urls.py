# app/inventory/urls.py

# Import from django/third parties modules
from django.urls import path

from app.inventory.views import CategoryView 

app_name = 'inventory'

urlpatterns = [
    path('categories/',CategoryView.as_view(),name="category_list"),
]
