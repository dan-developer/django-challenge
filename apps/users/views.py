from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import UserSerializer


class UserList(views.APIView):
    """
    List all users, or create a user.
    """

    def get(self, request):
        objs = get_user_model().objects.all()
        serializer = UserSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(views.APIView):
    """
    Retrieve, update or delete a user.
    """

    def get_object(self, pk):
        user_model = get_user_model()
        return get_object_or_404(user_model, pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = UserSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = UserSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        serializer = UserSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class UserViewset(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#     @action(detail=True)
#     def balance(self, request, pk):
#         user = self.get_object()
#         transaction_in_balance = Transaction.objects.filter(user=user, type=Transaction.TYPE_IN).aggregate(Sum('value'))['value__sum'] or 0
#         transaction_out_balance = Transaction.objects.filter(user=user, type=Transaction.TYPE_OUT).aggregate(Sum('value'))['value__sum'] or 0
#         return Response({
#             'balance': float(transaction_in_balance) - float(transaction_out_balance0)
#         })
