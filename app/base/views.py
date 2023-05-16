from django.shortcuts import render
from django.views import generic 

# Create your views here.

# def home_page(request):
# 	return render(request, 'base/index.html')

class home_page(generic.TemplateView):
	template_name = 'base/home.html'
