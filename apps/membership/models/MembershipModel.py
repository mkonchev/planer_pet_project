from django.db import models

from apps.membership.models.admins.MembershipModelAdmin import (
    MembershipModelAdmin,
)
from config.constants import NULLABLE


class Membership(models.Model):
    ModelAdmin = MembershipModelAdmin

    group = models.ForeignKey('group.Group', on_delete=models.PROTECT)
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    inviter = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64, **NULLABLE)

    class Meta:
        verbose_name = 'Зависимость'
        verbose_name_plural = 'Зависимости'

    def __str__(self):
        return f'{self.group} {self.user}'
