from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework.response import Response
from django.contrib.auth.models import User
import random

def generate_4_digit_code():
    return str(random.randint(1000, 9999))


class RegisterStartAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get("username")
        last_name = data.get("last_name")
        password = data.get("password")
        if not username or not last_name or not password:
            return Response({"message":"siz qaysidirga malumot kiritmadingiz"})
        else:
            request.session["step1"]={
                "username" : username,
                "last_name" : last_name,
                "password"  : password
        }
            return Response({"message":"1-bosqichdan ordingiz"})      
      

class RegisterBirthAPIView(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email")
        if not email:
            return Response({"message":"emailni kiritmadingiz"})
        step1 = request.session.get("step1")
        password_for_complete=generate_4_digit_code()
        request.session["step2"]={
            "email" : email,
            "password_for_complete": password_for_complete
        }
        return Response({"message":"2-bosqichdan otdingiz"})
        

class RegisterCompleteAPIView(APIView):
    def post(self,request):
        step1 = request.session.get("step1")
        step2 = request.session.get("step2")
        data = request.data
        password_chack = data.get("password_chack")
        password_for_complete = step2.get("password_for_complete")
        print(password_for_complete)
        if not password_chack:
            return Response({"message":"siz password  kiritmadingiz"})
        if password_chack == password_for_complete:
            username = step1.get("username")
            last_name = step1.get("last_name")
            password = step1.get("password")
            email = step2.get("email")
            user = User.objects.create(
                username = username,
                last_name = last_name,
                email = email,
                is_active=True
            )
            user.set_password(password)
            user.save()
            request.session.pop("register_step1", None)
            request.session.pop("register_step2", None)
            return Response({"message":"Siz registratsiyadan toliq otdingiz!"})





class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
