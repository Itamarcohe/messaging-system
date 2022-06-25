from .serializers import (  UserRegistrationSerializer, 
                            UserLoginSerializer,
                            UserSerializer)
from rest_framework import generics, permissions, response

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserLoginAPIView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        access_token = RefreshToken.for_user(user).access_token

        return response.Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": str(access_token)
        })