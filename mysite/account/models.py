from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings


class UserModel(AbstractUser):
    name = models.CharField(max_length=216, null = False, blank = False)
    slug = models.SlugField(unique = True, null = False, blank = False)
    user_logs = models.TextField(default='',null = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(UserModel, self).save(*args, **kwargs)
