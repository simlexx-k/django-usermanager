# accounts/urls.py
from django.urls import path
from .views import register, user_login, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
