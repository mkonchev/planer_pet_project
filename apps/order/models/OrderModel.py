from django.db import models

from apps.order.models.admins.OrderModelAdmin import OrderModelAdmin
from apps.order.models.consts import OrderPaymentTypeChoice, OrderStatusChoice
from config.constants import NULLABLE


class PaymentInfo(models.Model):
    created_at = models.DateTimeField(verbose_name='Время заказа', auto_now_add=True)
    pay_at = models.DateTimeField(verbose_name='Время подтверждения оплаты', auto_now_add=True)

    class Meta:
        abstract = True


class Order(PaymentInfo):
    ModelAdmin = OrderModelAdmin

    cost = models.PositiveIntegerField(verbose_name='Цена подписки')
    payment_type = models.PositiveIntegerField(
        verbose_name='Тип оплаты',
        choices=OrderPaymentTypeChoice,
        default=OrderPaymentTypeChoice.sbp
    )
    payment_external_id = models.PositiveIntegerField(verbose_name='ID платежа')
    status = models.PositiveIntegerField(
        verbose_name='Статус оплаты',
        choices=OrderStatusChoice,
        default=OrderStatusChoice.none
    )
    user = models.ForeignKey(
        'core.User',
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        related_name='orders',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Тут будет id'
