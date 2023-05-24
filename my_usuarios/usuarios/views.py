from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .models import Users
from .serializers import UsersSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    

