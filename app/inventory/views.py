# app/inventory/views.py

# Import django/third parties modules
from django.shortcuts import render
from django.views.generic import ListView, CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy 

# Import from locals
from app.inventory.models import Category
from app.inventory.forms import CategoryForm

# Create your views here.

class CategoryView(LoginRequiredMixin,ListView):
	model = Category
	template_name = 'inventory/category_list.html'
	context_object_name = 'obj'
	login_url = 'users:login' 


class CategoryNew(LoginRequiredMixin,CreateView):
	model=Category
	template_name="inventory/category_form.html"
	context_object_name="obj"
	form_class=CategoryForm
	success_url=reverse_lazy("inventory:category_list")
	login_url="users:login"

	def form_valid(self, form):
		form.instance.user_creation = self.request.user 
		return super().form_valid(form)