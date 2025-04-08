from django.db import models


class StoreCategoryChoice(models.IntegerChoices):
    apps = 0, 'Минуты в приложениях'
    habits = 1, 'Вредные привычки'
