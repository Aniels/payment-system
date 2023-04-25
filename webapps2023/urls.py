from django.contrib import admin
from django.urls import path, include
from interface import views as interface

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('webapps2023/', include('interface.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls')),
    path('', interface.bring_home, name='redirect')
]