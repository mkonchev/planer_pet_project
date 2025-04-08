from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.managers.UserManager import UserManager
from config.constants import NULLABLE


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    balance = models.PositiveIntegerField(verbose_name='Баланс', default=0)
#    group_id
    sub_active = models.BooleanField(verbose_name='Подписка', default=False)
    sub_due_to_date = models.DateTimeField(verbose_name='Активна до', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
