from django.urls import path

from app.base import views 

app_name = 'base'

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('',views.Home.as_view(),name="home")
]
