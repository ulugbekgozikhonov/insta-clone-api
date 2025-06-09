from rest_framework import serializers
from general.utils import is_valid_email, is_valid_phone_number
from users.models import User, AUTH_STATUS_NEW, AUTH_STATUS_DATE, AUTH_STATUS_DONE, AUTH_TYPE_EMAIL, AUTH_TYPE_PHONE
from datetime import datetime, timedelta
from django.db.models import Q

class UserStep1Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)
    fullname = serializers.CharField(max_length=30)
    email_or_phone = serializers.CharField(max_length=100)

    def validate_email_or_phone(self, value):
        if not (is_valid_email(value) or is_valid_phone_number(value)):
            raise serializers.ValidationError("Invalid email or phone number format.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate(self, attrs):
        email_or_phone = attrs.get("email_or_phone")

        if is_valid_email(email_or_phone):
            attrs["email"] = email_or_phone
        elif is_valid_phone_number(email_or_phone):
            attrs["phone"] = email_or_phone
        return attrs

    def create(self, validated_data):
        email = validated_data.pop("email", None)
        phone = validated_data.pop("phone", None)

        user = User(
            username=validated_data["username"],
            first_name=validated_data["fullname"].split()[0],
            last_name=" ".join(validated_data["fullname"].split()[1:]),
            email=email,
            phone_number=phone,
            auth_type=AUTH_TYPE_EMAIL if email else AUTH_TYPE_PHONE,
            auth_status=AUTH_STATUS_NEW,
            is_active=False
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class UserStep2Serializer(serializers.Serializer):
    date_of_birth = serializers.DateField(required=True, write_only=True)
    username = serializers.CharField(max_length=100, required=True, write_only=True)
    

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username is required.")
        return value
    
    def validate_date_of_birth(self, value):
        now = datetime.now().date()
        if now - value < timedelta(days=365 * 16):
            raise serializers.ValidationError("User must be at least 16 years old.")
        return value

    def save(self, **kwargs):
        username = self.validated_data.get("username")
        date_of_birth = self.validated_data.get("date_of_birth")

        user = User.objects.filter(username=username, auth_status=AUTH_STATUS_NEW).first()

        if not user:
            raise serializers.ValidationError("User not found.")

        user.date_of_birth = date_of_birth
        user.auth_status = AUTH_STATUS_DATE
        user.save()
        return user
