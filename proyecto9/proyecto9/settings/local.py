from .base import *

SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "settings"),
}


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'ENGINE': 'mssql',
        'NAME':'DBProyecto9',
        'USER': 'dragonhak',
        'PASSWORD': 'josejose',
        'HOST': 'localhost\SQLEXPRESS',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
