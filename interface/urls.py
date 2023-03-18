from django.urls import path
from . import views

urlpatterns = [
    path('', views.wellcome, name='wellcome'),
    path('login/client/', views.login_client, name='login-client'),
    path('login/admin/', views.login_admin, name='login-admin'),
    path('register/', views.register, name='register'),
    path('loading/', views.loading, name='loading'),

]
