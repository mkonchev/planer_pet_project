from django.db import models
from apps.user.models.admins.UserModelAdmin import UserModelAdmin

class User(models.Model):
    ModelAdmin = UserModelAdmin

    name = models.CharField(verbose_name='Имя пользователя', max_length=100, default='_')
    email = models.CharField(verbose_name='e-mail', max_length=100, default='_')
    password = models.CharField(verbose_name='Пароль', max_length=100, default='_')
    balance = models.PositiveIntegerField(verbose_name='Баланс')
#    group_id
    sub_active = models.BooleanField(verbose_name='Подписка')
    sub_due_to_date = models.DateTimeField(verbose_name='Активна до', auto_now_add=True)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

    def __str__(self):
        return self.name