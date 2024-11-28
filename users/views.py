from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserCreateAPIView(generics.CreateAPIView):
    """API CREATE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
