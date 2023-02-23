from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.serializers import TokenVerifySerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass


class CustomTokenVerifySerializer(TokenVerifySerializer):
    pass
