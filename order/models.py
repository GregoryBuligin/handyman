from django.db import models

from account.models import Account
from service.models import Service

# Create your models here.

class Order(models.Model):
    """( description)"""
    account = models.ForeignKey(
        Account,
        related_name='accound',
        db_index=True
    )
    service = models.ForeignKey(
        Service,
        related_name='service',
        db_index=True
        )
    staff = models.ForeignKey(
        Account,
        related_name='masters',
        db_index=True
    )
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return 'Order {}:: {}|{}|{}| \n {}'.format(
            self.pk,
            self.account_id,
            self.service_id,
            self.staff_id,
            self.price
        )

    class Meta:
        db_table = "User_Order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['service_id']
