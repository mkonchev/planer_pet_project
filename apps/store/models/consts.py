from django.db import models

class StoreCategoryChoice(models.IntegerChoices):
    apps = 0, 'Приложение'
    #minutes = 1, 'Минуты'...
    