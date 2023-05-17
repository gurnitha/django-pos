# app/inventory/urls.py

# Import from django/third parties modules
from django.urls import path

from app.inventory.views import CategoryView, CategoryNew 

app_name = 'inventory'

urlpatterns = [
    path('categories/',CategoryView.as_view(),name="category_list"),
    path('categories/new',CategoryNew.as_view(),name="category_new"),
]
