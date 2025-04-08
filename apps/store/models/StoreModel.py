from django.db import models

from apps.store.models.admins.StoreModelAdmin import StoreModelAdmin
from apps.store.models.consts import StoreCategoryChoice


class Store(models.Model):
    ModelAdmin = StoreModelAdmin

    price = models.PositiveIntegerField(verbose_name='Цена покупки')
    category = models.PositiveIntegerField(
        verbose_name='Категория',
        choices=StoreCategoryChoice.choices,
        default=StoreCategoryChoice.apps
    )
    name = models.CharField(verbose_name='Название', max_length=100, default='-')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
