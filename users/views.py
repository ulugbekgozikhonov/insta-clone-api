from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # Save the user data to the database
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)
