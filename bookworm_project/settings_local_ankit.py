from .settings_base import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ENV = 'local'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_SUBJECT_PREFIX = "[Bookworm Ankit Local] "

ADMINS = (
    ('Ankit Agarwal', 'ankitagarwal24.8@gmail.com'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': 'bookworm_ankit_local - '
                      '[%(name)s]- '
                      '%(levelname)s- '
                      '%(asctime)s '
                      # '%(filename)s: %(lineno)d - '
                      #   '%(funcName)s '
                      '%(message)s',
        },
    },
    'filters': {
    },
    'handlers': {
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     # 'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'formatter': 'standard',
        # },
        'sys_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'standard',
            'address': ('logs3.papertrailapp.com', 0000),
        }
    },
    'loggers': {
        '': {
            'handlers': [],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
