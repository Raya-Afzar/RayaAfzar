# company/model.py

from django.db import models

from mysite.core.models import TimeStampedModel

class ContactUsModel(TimeStampedModel):
    name = models.CharField(max_length = 264, blank = False, null = False)
    email = models.EmailField(blank = True, null = True)
    phone_number = models.CharField(max_length = 13, blank = True, null =True)
    request = models.TextField(null = True, blank = True)
