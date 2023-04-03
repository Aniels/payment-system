from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views as interface_view
from register import views as register_view

urlpatterns = [
    path('', interface_view.home, name='home'),
    path('login/', LoginView.as_view(template_name='authenticate/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view.register, name='register'),
    path('profile/', interface_view.profile, name='profile'),
]
