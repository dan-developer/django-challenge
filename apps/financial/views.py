from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListByUser(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        Return the list of transactions base on user ID passed by GET param.
        """
        user_id = self.kwargs['user_id']
        user = get_object_or_404(get_user_model(), id=user_id)
        return Transaction.objects.filter(user=user).order_by('inserted_at').all()


class TransactionUserBalance(views.APIView):
    def get(self, request, user_id):
        transaction_in_balance = Transaction.objects.filter(user__id=user_id, type=Transaction.TYPE_IN).aggregate(Sum('value'))['value__sum'] or 0
        transaction_out_balance = Transaction.objects.filter(user__id=user_id, type=Transaction.TYPE_OUT).aggregate(Sum('value'))['value__sum'] or 0
        return Response({
            'balance': float(transaction_in_balance) - float(transaction_out_balance)
        })


class TransactionList(views.APIView):
    """
    List all transactions, or create a transaction.
    """

    def get(self, request):
        transactions = Transaction.objects.order_by('inserted_at').all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetail(views.APIView):
    """
    Retrieve, update or delete a transaction.
    """

    def get_object(self, pk):
        return get_object_or_404(Transaction, pk=pk)

    def get(self, request, pk):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class TransactionViewset(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
