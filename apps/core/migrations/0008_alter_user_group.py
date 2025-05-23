# Generated by Django 5.0.3 on 2025-04-18 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_group'),
        ('membership', '0002_alter_membership_invite_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_group_in', to='membership.membership', verbose_name='Группа'),
        ),
    ]
