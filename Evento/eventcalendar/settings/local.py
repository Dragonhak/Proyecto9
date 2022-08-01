import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

#STATICFILES_DIRS = (
#    os.path.join(os.path.dirname(BASE_DIR), "static"),   
#)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'DBProyecto9',
        'USER': 'postgres',
        'PASSWORD': 'a',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}