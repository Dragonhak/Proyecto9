import os
from .base import *

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