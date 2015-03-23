# settings/production.py
from base import *

INSTALLED_APPS += ("gunicorn",)

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# TEMPLATE_DEBUG = False

# This does nothing with emails. Just for testing in Heroku
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
