from django.db import models
from apps.order.models.admins.OrderModelAdmin import OrderModelAdmin
from apps.order.models.consts import TaskPaymentTypeChoice, TaskStatusChoice

class Order(models.Model):
    ModelAdmin = OrderModelAdmin

    cost = models.PositiveIntegerField(verbose_name='Цена подписки')
    payment_type = models.PositiveIntegerField(verbose_name='Тип оплаты', choices=TaskPaymentTypeChoice, default=TaskPaymentTypeChoice.sbp)
    payment_external_id = models.PositiveIntegerField(verbose_name='ID платежа')
    status = models.PositiveIntegerField(verbose_name='Статус оплаты', choices=TaskStatusChoice, default=TaskStatusChoice.none)
    created_at = models.DateTimeField(verbose_name='Время заказа')
    pay_at = models.DateTimeField(verbose_name='Время подтверждения оплаты')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name