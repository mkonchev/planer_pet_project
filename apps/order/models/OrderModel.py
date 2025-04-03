from django.db import models
from apps.order.models.admins.OrderModelAdmin import OrderModelAdmin
from apps.order.models.consts import TaskPaymentTypeChoice, TaskStatusChoice

class PaymentInfo(models.Model):
    created_at = models.DateTimeField(verbose_name='Время заказа', auto_now_add=True)
    pay_at = models.DateTimeField(verbose_name='Время подтверждения оплаты', auto_now_add=True)

    class Meta:
        abstract = True

class Order(models.Model):
    ModelAdmin = OrderModelAdmin

    cost = models.PositiveIntegerField(verbose_name='Цена подписки')
    payment_type = models.PositiveIntegerField(verbose_name='Тип оплаты', choices=TaskPaymentTypeChoice, default=TaskPaymentTypeChoice.sbp)
    payment_external_id = models.PositiveIntegerField(verbose_name='ID платежа')
    status = models.PositiveIntegerField(verbose_name='Статус оплаты', choices=TaskStatusChoice, default=TaskStatusChoice.none)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name