# Email backend
import os
from core.settings.base import BASE_DIR

SECRET_KEY = 'django-insecure-mrk3h^2+7cas%6q$(6_gt!tixkx)=-)=m)l)id-c1qbm&r2df_'

DEBUG = False

ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CSRF_TRUSTED_ORIGINS = []

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
        },
    },
    'loggers': {
        '': { # empty string
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}