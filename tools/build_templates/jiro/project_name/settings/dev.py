from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'

INSTALLED_APPS += (
    'django_extensions',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

