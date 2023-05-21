# app/inventory/urls.py

# Import from django/third parties modules
from django.urls import path

from app.inventory.views import CategoryView, CategoryNew, CategoryEdit, CategoryDelete 

app_name = 'inventory'

urlpatterns = [
    path('categories',CategoryView.as_view(),name="category_list"),
    path('categories/new',CategoryNew.as_view(),name="category_new"),
    path('categories/edit/<int:pk>',CategoryEdit.as_view(),name="category_edit"),
    path('categories/delete/<int:pk>',CategoryDelete.as_view(),name="category_delete"),
]
