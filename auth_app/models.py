from django.contrib.auth.models import AbstractUser
from django.db import models


class SchoolUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(default=18, verbose_name='Возраст')
    is_teacher = models.BooleanField(default=False, verbose_name='Статус учителья')
    is_moderator = models.BooleanField(default=False, verbose_name='Статус модератора')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


