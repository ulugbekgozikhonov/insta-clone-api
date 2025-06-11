from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # Save the user data to the database
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)
    

class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "This is a test endpoint."}, status=200)
