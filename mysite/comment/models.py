# comment/models.py

from django.db import models
from django.utils import timezone

# handmade
from mysite.core.models import TimeStampedModel


class CommentModel(TimeStampedModel):
    project_name = models.CharField(max_length = 264, null = True, blank = True)
    person_name = models.CharField(max_length = 264, null = False, blank = False)
    comment = models.TextField(null = False, blank = False)
    picture = models.ImageField(blank = False, null = False,
                                upload_to=r'comment', default = r'comment/default/default.jpg')


class FamousCustomerModel(TimeStampedModel):
    picture = models.ImageField(default = r'comment/default/default.jpg',
                                 upload_to=r'comment/logos/')
    description = models.TextField(null = True, blank = True)
