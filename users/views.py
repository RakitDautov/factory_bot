from rest_framework import viewsets, permissions, status
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, PasswordSerializer
from .models import User

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]

    def perform_create(self, serializer):
        if "password" in self.request.data:
            password = make_password(self.request.data["password"])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        if "password" in self.request.data:
            password = make_password(self.request.data["password"])
            serializer.save(password=password)
        else:
            serializer.save()

    @action(["post"], detail=False)
    def set_password(self, request, *args, **kwargs):
        user = self.request.user
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return Response({"status": "password set"})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        