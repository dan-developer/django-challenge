from rest_framework import serializers
from apps.financial.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('type', 'value', 'user', 'inserted_at')
