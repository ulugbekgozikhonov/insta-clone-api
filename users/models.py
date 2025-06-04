from general.models import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    GENDER_TYPES = (("male", "Male"), ("female", "Female"))
    VERIFY_TYPES = (("email", "Email"), ("phone", "Phone"))
    AUTH_STATES = (
        ("begin", "Begin"),
        ("date_of_birth", "Date of Birth"),
        ("verified", "Verified"),
        ("completed", "Completed"),
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    gender = models.CharField(
        max_length=10, choices=GENDER_TYPES, null=True, blank=True
    )
    verify_type = models.CharField(max_length=10, choices=VERIFY_TYPES)
    auth_state = models.CharField(max_length=20, choices=AUTH_STATES)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
