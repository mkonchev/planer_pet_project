from django.db import models

from apps.group.models.admins.GroupModelAdmin import GroupModelAdmin
from config.constants import NULLABLE


class Group(models.Model):
    ModelAdmin = GroupModelAdmin

    owner = models.ForeignKey(
        'core.User',
        verbose_name='Администратор',
        on_delete=models.PROTECT,
        related_name='owned_groups',
        **NULLABLE
    )
    name = models.CharField(verbose_name='Название группы', max_length=100)
    slug = models.CharField(verbose_name='Идентификатор группы', **NULLABLE, max_length=200)
    members = models.ManyToManyField(
            'core.User',
            verbose_name='Участники',
            related_name='group_members',
            through='membership.Membership',
            through_fields=('group', 'user')
        )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.slug

    def get_members(self):
        return ', '.join([p.email for p in self.members.all()])
