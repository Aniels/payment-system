from rest_framework import serializers
from payapp.models.currency import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'currency_code', 'country', 'rate')
