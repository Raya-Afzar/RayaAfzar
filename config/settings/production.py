from .base import *
import json

with open('/home/raya_afzar/django_env/config.json') as config_file:
    config = json.load(config_file)

DEBUG = False
SECRET_KEY = config['SECRET_KEY']

ALLOWED_HOSTS = ['*',]

ALLOWED_HOSTS = [config['ALLOWED_HOST1'],config['ALLOWED_HOST2'],config['ALLOWED_HOST3']
                    ,config['ALLOWED_HOST4'],config['ALLOWED_HOST5']]
                    

INSTALLED_APPS = INSTALLED_APPS + ['dbbackup',]                    


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config['DATABASE_NAME'],
        'USER': config['DATABASE_USER'],
        'PASSWORD': config['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432'
    }
}



#Backup
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/home/server_user/backup/'}


SECURE_HSTS_SECONDS = 259200
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

#SESSION_COOKIE_SECURE = True

