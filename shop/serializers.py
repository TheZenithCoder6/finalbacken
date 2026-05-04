from rest_framework import serializers
from .models import Product, Artist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User  # ✅ Optional, rahne de

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TopArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'image', 'short_about']
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # ✅ Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # ✅ Response mein bhi email bhejo
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data