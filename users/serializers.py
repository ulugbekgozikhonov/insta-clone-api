from rest_framework import serializers
from general.utils import is_valid_email, is_valid_phone_number


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)
    fullname = serializers.CharField(max_length=30)
    email_or_phone = serializers.CharField(max_length=100)    
    