# app/inventory/views.py

# Import django/third parties modules
from django.shortcuts import render
from django.views.generic import ListView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Import from locals
from app.inventory.models import Category

# Create your views here.

class CategoryView(LoginRequiredMixin, ListView):
	model = Category
	template_name = 'inventory/category_list.html'
	context_object_name = 'obj'
	login_url = 'users:login' 
