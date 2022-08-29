import os
from .base import *
"""
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
"""
#Prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'dfvr27b8bi81ev',
        'USER': 'lvyjyxjoeobxex',
        'PASSWORD': 'c432a0de802561fee1325802af57cbfdfbda143471ed0981e91e30b06996677b',
        'HOST': 'ec2-44-205-63-142.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
