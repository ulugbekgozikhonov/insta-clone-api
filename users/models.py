from general.models import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

AUTH_STATUS_NEW, AUTH_STATUS_DATE, AUTH_STATUS_DONE = "new", "date", "done"
AUTH_TYPE_EMAIL, AUTH_TYPE_PHONE = "email", "phone"

class User(AbstractUser, BaseModel):
    GENDER_TYPES = (("male", "Male"), ("female", "Female"))
    AUTH_TYPES = (
        (AUTH_TYPE_EMAIL, "Email"),
        (AUTH_TYPE_PHONE, "Phone")
    )
    AUTH_STATUS = (
        (AUTH_STATUS_NEW,"New"),
        (AUTH_STATUS_DATE, "Date"),
        (AUTH_STATUS_DONE, "Done"),
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True,validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])
        ]
    )
    gender = models.CharField(
        max_length=10, choices=GENDER_TYPES, null=True, blank=True
    )
    auth_type = models.CharField(max_length=10, choices=AUTH_TYPES)
    auth_status = models.CharField(max_length=20, choices=AUTH_STATUS)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

class UserVerification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="verifications")
    code = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    expiration_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.code}"
    