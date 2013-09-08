from django.utils.translation import ugettext as _
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import os
import socket

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DEBUG = False if socket.gethostname() == 'moscowtrip' else True
TEMPLATE_DEBUG = DEBUG

# --------------------------------------------------------------------------------------------------
# Commons
# --------------------------------------------------------------------------------------------------
ALLOWED_HOSTS = []
SECRET_KEY = 'o&%s+vcs-1$-4yvm-ezffl1#xu104%=wf%(wu_c2b3#kykz@oq'
SITE_ID = 1
ROOT_URLCONF = 'apps.main.urls'
WSGI_APPLICATION = 'config.wsgi.application'
AUTH_USER_MODEL = 'accounts.User'
FIXTURE_DIRS = (os.path.join(PROJECT_ROOT, 'fixtures'), )

DATE_INPUT_FORMATS = ('%m.%d.%Y', )

ADMINS = (
    ('Vitaliy Korobkin', 'vitalisbox@gmail.com'),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',
    'django.contrib.admin',
    'south',
    'auth_pack',
    'apps.main',
    'apps.accounts',
    'django_countries'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# --------------------------------------------------------------------------------------------------
# Langs & Time
# --------------------------------------------------------------------------------------------------
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'en-en'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------------------------------------------------------------------------------
# Static
# --------------------------------------------------------------------------------------------------
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = '' if DEBUG else '/home/deploy/moscowtrip-static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    (os.path.join(PROJECT_ROOT, 'static/')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# --------------------------------------------------------------------------------------------------
# Django settings
# --------------------------------------------------------------------------------------------------
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

DEFAULT_FROM_EMAIL = 'info@travelatus.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


SENDGRID_SETTINGS = dict(
        username="travelatus",
        password="ksqRfD4IZDrbFFt",
        secure=True,
)

# --------------------------------------------------------------------------------------------------
# Django Suit
# --------------------------------------------------------------------------------------------------
SUIT_CONFIG = {
    'ADMIN_NAME': 'Site Name',
    'MENU': (
        {
            'app': 'accounts',
            'models': ('accounts.user', 'auth.group'),
            'label': _('Users'), 'icon': 'icon-lock',
        },
    )
}

# --------------------------------------------------------------------------------------------------
# Logging
# --------------------------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
