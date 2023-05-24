from django.contrib import admin
from django.urls import path, include
from usuarios.views import UserListAPIView, UserCreateAPIView
from rest_framework import routers


urlpatterns = [
    path('api/users/', UserListAPIView.as_view(), name='user-list'),
    path('api/users/create/', UserCreateAPIView.as_view(), name='user-create'),
]

