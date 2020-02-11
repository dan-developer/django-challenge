from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
