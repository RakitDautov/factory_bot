from django.core.management.base import BaseCommand

import os

from dotenv import load_dotenv
from telegram.ext import Updater, Filters, MessageHandler
from users.models import User


load_dotenv()


def put_chat_id(update, context):
    """Ищит пользователя по токену и заполняет поле chat_id"""
    chat = update.effective_chat
    token = update.message.text
    user = User.objects.get(auth_token=token)
    context.bot.send_message(chat_id=chat.id, text=f"Привет, {user.first_name}!")
    user.chat_id = chat.id
    user.save()


class Command(BaseCommand):
    """Бот слушает telegram, любое сообщение принимается как Token"""
    def handle(self, *args , **options):
        updater = Updater(token=os.getenv('TELEGRAM_TOKEN'))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, put_chat_id))
        updater.start_polling()
        updater.idle()
