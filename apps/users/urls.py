from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]
