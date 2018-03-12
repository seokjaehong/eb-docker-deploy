from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())

set_config(secrets, module_name=__name__, start=True)
# print(getattr(sys.modules[__name__], 'DATABASES'))

DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
]
WSGI_APPLICATION = 'config.wsgi.production.application'

INSTALLED_APPS += [
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'
