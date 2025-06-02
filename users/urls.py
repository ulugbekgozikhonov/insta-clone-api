from django.urls import path
from users import views




urlpatterns = [
    path('register/',views.RegisterAPIView.as_view(),name='register'),
    path('users/',views.UsersListAPIView.as_view(),name='users-list')
]