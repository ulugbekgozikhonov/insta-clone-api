from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserStep1Serializer, UserStep2Serializer
from users.models import User, AUTH_STATUS_NEW
from django.db.models import Q

class RegisterAPIView1(APIView):
    def post(self, request):
        data = request.data
        serializer = UserStep1Serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # Save the user data to the database
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)

class RegisterAPIView2(APIView):
    def post(self, request):
        data = request.data
        serializer = UserStep2Serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # Save the user data to the database
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)