from .base import *

SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "settings"),
}


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'Servidor1',
        'USER': 'dragonhak',
        'PASSWORD': 'josejose',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    }
}
