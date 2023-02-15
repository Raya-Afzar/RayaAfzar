# order/models.py
from django.db import models

from mysite.core.models import TimeStampedModel


class OrderModel(TimeStampedModel):
    name = models.CharField(max_length = 264, blank = False, null = False)
    phone_number = models.CharField(max_length = 13, blank = False, null = False)
    title = models.CharField(max_length = 264, blank = False, null = False)
    description = models.TextField(null = True, blank = True)
    checked = models.BooleanField(default = False)

    def __str__(self):
        return self.phone_number
