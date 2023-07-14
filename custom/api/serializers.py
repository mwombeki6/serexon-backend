from rest_framework import serializers
from custom.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_customer', 'is_vendor']
        
