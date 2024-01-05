from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        # 여기 있어야 DB에 기록된다..!
        fields = ('username', 'email', 'password',)
