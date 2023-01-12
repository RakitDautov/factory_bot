from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Модель пользователя"""

    username = models.CharField(verbose_name='Логин пользователя', unique=True, max_length=50)
    first_name = models.CharField(verbose_name='Имя пользователя', max_length=50)
    chat_id = models.IntegerField(verbose_name='id пользователя telegram', default=0, blank=True)
