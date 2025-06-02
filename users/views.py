from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializers



class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
