from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    phone = models.CharField(verbose_name='Phone', max_length=14, null=True, default=None)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        ordering = ['-id']
        db_table = 'auth_user'
