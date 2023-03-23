from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('loading/', views.loading, name='loading'),
    path('gpt/', views.gpt, name='gpt')

]
