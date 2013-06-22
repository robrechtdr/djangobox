from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SECONDARY_PATH,
          'db/{{ project_name }}.db'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATIC_URL = '/static/'

INSTALLED_APPS += (
    'django_extensions',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

