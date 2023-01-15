from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerialiser


class MessageView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MessageSerialiser

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Message.objects.filter(author=self.request.user)
