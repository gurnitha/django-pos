from django.urls import path
from django.contrib.auth import views as auth_views

from app.users import views 

app_name = 'users'

urlpatterns = [
    # path('login',views.Login.as_view(),name="login")
    path('login/',auth_views.LoginView.as_view(
            template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(
            template_name='users/logout.html'),name="logout")
]
