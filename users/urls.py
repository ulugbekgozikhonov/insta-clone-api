from django.urls import path
from users import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    path("test/", views.TestAPIView.as_view(), name="test"),
]
