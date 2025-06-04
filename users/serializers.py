from rest_framework import serializers
from .myregex import is_valid_email, is_valid_phone_number
from users.models import User


class UserSerializer(serializers.Serializer):
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
            verify_type="email" if email else "phone",
            auth_state="begin",
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
