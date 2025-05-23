# Generated by Django 5.0.3 on 2025-04-18 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_remove_membership_group_remove_membership_inviter_and_more'),
        ('membership', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='group_members', through='membership.Membership', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
    ]
