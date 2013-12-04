from common import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES['default'] =  dj_database_url.config()

INSTALLED_APPS += (
    'gunicorn',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

