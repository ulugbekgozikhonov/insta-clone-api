from django.urls import path
from users import views




urlpatterns = [
    path('register1/',views.RegisterStartAPIView.as_view(),name='register1'),
    path('register2/',views.RegisterBirthAPIView.as_view(),name='register2'),
    path('register3/',views.RegisterCompleteAPIView.as_view(),name='register3'),
    path('users/',views.UsersListAPIView.as_view(),name='users-list')
]