import os
from dotenv import load_dotenv

from rest_framework import viewsets, permissions

from telegram import Bot

from .models import Message
from .serializers import MessageSerialiser


load_dotenv()


class MessageView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MessageSerialiser

    def send_mess(self, text, chat_id):
        """Отправляет сообщение пользователю после сохранения"""
        bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
        bot.send_message(chat_id, text) 

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        try:
            text = self.request.data.get('text')
            self.send_mess(text=text, chat_id=user.chat_id)
        except Exception:
            print('Chat_id или текст сообщения не корректны')

    def get_queryset(self):
        return Message.objects.filter(author=self.request.user)
    

