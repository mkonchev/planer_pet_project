from django.db import models

from apps.task.models.admins.TaskModelAdmin import TaskModelAdmin
from apps.task.models.consts import TaskCategoryChoice


class Task(models.Model):
    ModelAdmin = TaskModelAdmin

    name = models.CharField(verbose_name="Задание", max_length=100, default="-")
    description = models.CharField(verbose_name="Описание задания", max_length=200, default="-")
    category = models.PositiveIntegerField(
        verbose_name="Категория",
        choices=TaskCategoryChoice.choices,
        default=TaskCategoryChoice.home
    )
#   user_id = models.PositiveIntegerField
    start_date = models.DateTimeField(verbose_name="Время начала задания")
    end_date = models.DateTimeField(verbose_name="Дедлайн")
    price = models.PositiveIntegerField(verbose_name="Награда за выполение задания")

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.name
