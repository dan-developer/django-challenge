from django.contrib.auth import get_user_model
from django.db import models


class Transaction(models.Model):

    TYPE_IN = 1
    TYPE_OUT = 2
    TYPE_CHOICES = (
        (TYPE_IN, 'In'),
        (TYPE_OUT, 'Out')
    )

    type = models.SmallIntegerField(verbose_name='Type', choices=TYPE_CHOICES, db_index=True)
    value = models.DecimalField(verbose_name='Value', max_digits=19, decimal_places=2)
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    inserted_at = models.DateTimeField(verbose_name='Inserted at', auto_now_add=True)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        db_table = 'transaction'
