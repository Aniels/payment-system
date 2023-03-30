from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.registration, name='register'),
    path('profile/', views.profile, name='profile'),
    path('gpt/', views.gpt, name='gpt'),
]
