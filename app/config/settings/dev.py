from .base import *

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'django_extensions',
]

secrets = json.loads(open(SECRETS_DEV, 'rt').read())

set_config(secrets, module_name=__name__, start=True)
print(getattr(sys.modules[__name__], 'DATABASES'))

DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
STATICFILES_STORAGE = 'config.storage.StaticFileStorage'