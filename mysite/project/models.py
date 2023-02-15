# project/model.py

from django.db import models
from django_jalali.db import models as jmodels

from mysite.core.models import TimeStampedModel

class ProjectModel(TimeStampedModel):

    Type_Website = 'web'
    Type_Desktop = 'dsk'
    Type_Plugin = 'plg'
    Type_Other = 'oth'

    Program_Types = (
    (Type_Website, 'Website'),
    (Type_Desktop, 'Dektop'),
    (Type_Plugin, 'Plugin'),
    (Type_Other, 'Other'),
    )

    name = models.CharField(max_length = 264, blank = False, null = False)
    client = models.CharField(max_length = 264, blank = True, null = True)
    url = models.URLField(blank = True, null = True)
    program_type = models.CharField(max_length = 3, choices = Program_Types, blank = True, null = True)
    production_date = jmodels.jDateField(blank = True, null = True)
    description = models.TextField(null = True, blank = True)

    picture_1 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_2 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_3 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_4 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_5 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_6 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_7 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_8 = models.ImageField(blank = True, null = True, upload_to=r'projects')
    picture_9 = models.ImageField(blank = True, null = True, upload_to=r'projects')
