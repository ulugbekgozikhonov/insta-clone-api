from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'last_name','email']
    
  