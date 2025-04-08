from django.db import models


class OrderPaymentTypeChoice(models.IntegerChoices):
    tink = 0, 'Т-банк'
    sber = 1, 'Сбер'
    sbp = 2, 'СБП'


class OrderStatusChoice(models.IntegerChoices):
    none = 0, '-'
    checking = 1, 'На проверке'
    success = 2, 'Успешно'
    error = 3, 'Ошибка'
