from rest_framework import serializers
from .models import Message

from users.serializers import UserSerializer


class MessageSerialiser(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Message
        fields = ['text', 'author', 'date']
