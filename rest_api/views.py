from .serializers import CurrencySerializer
from payapp.models.currency import Currency
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class ConversionApiView(APIView):
    def get(self, request, c1_id, c2_id, c1_amount):
        c1 = Currency.objects.get(pk=c1_id)
        c2 = Currency.objects.get(pk=c2_id)
        converse_result = c1_amount * (c2.rate/c1.rate)
        conversion = {
            'source currency': c1.currency_code,
            'target currency': c2.currency_code,
            'conversed result': converse_result
        }
        return Response(conversion)


class ListCurrencyAPIView(ListAPIView):
    # Lists all Currency from the database
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CreateCurrencyAPIView(CreateAPIView):
    # Creates a new Currency
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class UpdateCurrencyAPIView(UpdateAPIView):
    # Update the Currency by id
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class DeleteCurrencyAPIView(DestroyAPIView):
    # Deletes the Currency by id
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
