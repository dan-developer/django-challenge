from django.urls import path, include
from . import views

app_name = 'financial'

urlpatterns = [
    path('transaction/user/<int:user_id>/', views.TransactionListByUser.as_view(), name='transactions-by-user-id'),
    path('transaction/user/<int:user_id>/balance/', views.TransactionUserBalance.as_view(), name='transactions-balance-by-user-id'),

    path('transaction/', views.TransactionList.as_view(), name='transaction-list'),
    path('transaction/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
]
