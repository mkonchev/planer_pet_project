from django.db import models


class TaskCategoryChoice(models.IntegerChoices):
    sport = 0, 'Спорт'
    edu = 1, 'Учеба'
    work = 2, 'Работа'
    home = 3, 'Дом'


class TaskStatusChoice(models.IntegerChoices):
    future = 0, 'Нужно сделать'
    in_progress = 1, 'В процессе'
    done = 2, 'Сделано'
