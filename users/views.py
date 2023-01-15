from rest_framework import viewsets, permissions
from django.contrib.auth.hashers import make_password

from .serializers import UserSerializer
from .models import User


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]

    def perform_create(self, serializer):
        password = make_password(self.request.data["password"])
        serializer.save(password=password)


    def perform_update(self, serializer):
        if "password" in self.request.data:
            password = make_password(self.request.data["password"])
            serializer.save(password=password)
        else:
            serializer.save()
        