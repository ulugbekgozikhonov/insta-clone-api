from general.models import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser, BaseModel):
    GENDER_TYPES = (("male", "Male"), ("female", "Female"))
    AUTH_TYPES = (("email", "Email"), ("phone", "Phone"))
    AUTH_STATUS = (
        ("new", "New"),
        ("date", "Date"),
        ("done", "Done"),
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
