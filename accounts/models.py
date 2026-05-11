from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Расширенная модель пользователя для ЛокоТех-Сервис
    """
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        blank=True
    )
    company = models.CharField(
        max_length=200,
        verbose_name='Предприятие',
        blank=True
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Должность',
        blank=True
    )

    # Поле для аватарки
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name='Аватар',
        blank=True,
        null=True,
        help_text='Загрузите изображение (PNG, JPG, JPEG)'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        """Возвращает URL аватарки или стандартную заглушку"""
        if self.avatar:
            return self.avatar.url
        return '/static/img/default-avatar.png'