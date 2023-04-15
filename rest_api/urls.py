from django.urls import path, register_converter
from .converters import FloatConverter
from .views import *


register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', ListCurrencyAPIView.as_view()),
    path('conversion/<int:c1_id>/<int:c2_id>/<float:c1_amount>', ConversionApiView.as_view(), name='my_api_view'),
    path('update/<int:pk>/', UpdateCurrencyAPIView.as_view()),
    path('create/', CreateCurrencyAPIView.as_view()),
    path('delet/<int:pk>', DeleteCurrencyAPIView.as_view()),
]
