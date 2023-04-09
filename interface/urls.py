from django.urls import path
from . import views as interface_view
from register import views as register_view
from payapp import views as payapp_view

urlpatterns = [
    path('', interface_view.home, name='home'),
    path('login/', register_view.login_view, name='login'),
    path('logout/', register_view.logout_view, name='logout'),
    path('register/', register_view.register, name='register'),
    path('profile/', interface_view.profile, name='profile'),
    path('transfer/', payapp_view.transfer, name='transfer'),
]
