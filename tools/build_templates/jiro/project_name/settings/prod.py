from common import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "postgredb",
        'USER': 'my_username',                      # Not used with sqlite3.
        'PASSWORD': 'my_password',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DATABASES['default'] =  dj_database_url.config()

INSTALLED_APPS += (
    'gunicorn',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

