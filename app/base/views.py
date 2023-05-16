from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView 

# Create your views here.

# def home_page(request):
# 	return render(request, 'base/index.html')

class Home(LoginRequiredMixin, TemplateView):
	template_name = 'base/index.html'
	# login_url = '/admin'
	login_url = 'users:login'
