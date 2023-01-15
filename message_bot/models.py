from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Message(models.Model):
    """Модель сообщения"""

    author = models.ForeignKey(
        User, verbose_name="Автор сообщения",
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
            verbose_name="Дата отправки", 
            auto_now_add=True
            )
    text = models.TextField(verbose_name="Текст сообщения")

    class Meta:
        ordering = [
            "date",
        ]
