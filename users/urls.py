from django.urls import path
from users import views

urlpatterns = [
    path("register/", views.RegisterAPIView1.as_view(), name="register"),
    path("date-of-birth/", views.RegisterAPIView2.as_view(), name="date_of_birth"),
]
