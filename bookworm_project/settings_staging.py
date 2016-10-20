from .settings_base import *

BASE_URL = ''
ENV = 'staging'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_SUBJECT_PREFIX = "[Bookworm Staging] "


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': 'bookworm_staging - '
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
            'address': ('logs3.papertrailapp.com', 00000),
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