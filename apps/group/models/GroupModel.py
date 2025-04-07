from django.db import models

from apps.group.models.admins.GroupModelAdmin import GroupModelAdmin
from config.constants import NULLABLE


class Group(models.Model):
    ModelAdmin = GroupModelAdmin

    name = models.CharField(verbose_name='Название группы', max_length=100)
    slug = models.CharField(verbose_name='Идентификатор группы', **NULLABLE, max_length=200)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
