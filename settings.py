# ============================================================ IMPORTS ==

import os
import sys
from media import MEDIA_BUNDLES


# ============================================================ UTILS ==

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
gettext = lambda s: s


# ============================================================ DEBUG SETTINGS ==

DEBUG = True
TEMPLATE_DEBUG = DEBUG


# ============================================================ DJANGO SETTINGS == 

ADMINS = (
  ('nerdfiles', 'nerdfiles@gmail.com'),
)
MANAGERS = ADMINS

# Site ID
SITE_ID = 1

# URL Settings
ROOT_URLCONF = 'urls'


# ============================================================ LOCAL SETTINGS ==

TIME_ZONE = 'America/Chicago'
LANGUAGES = [('en', 'EN')]
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

# DB Settings
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'local-db.sqlite',
    #'USER': '',
    #'PASSWORD': '',
    #'HOST': '',
    #'PORT': '',
  }
}


# ============================================================ PATH SETTINGS ==

MEDIA_ROOT = PROJECT_DIR + '/_assets'
MEDIA_URL = '/_assets/'
"""
STATIC_ROOT = PROJECT_DIR + '/static'
STATIC_URL = '/static/'
"""
ADMIN_MEDIA_PREFIX = '/_assets/admin/'


# ============================================================ STATICFILES SETTINGS ==

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# ============================================================ SECRET KEY ==

SECRET_KEY = 'vo5jm=n(t5+8t!uuacs3y6ug45p6z#pil+f-$70(xaaa5t+k%q'


# ============================================================ TEMPLATE LOADERS ==

TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  'django.template.loaders.eggs.Loader',
)


# ============================================================ MIDDLEWARE SETTINGS ==

MIDDLEWARE_CLASSES = (
  # django.contrib.*
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  
  # django.middleware.*
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  
  # third-party middleware
  # ... additional middleware
)


# ============================================================ TEMPLATE CONTEXT PROCESSORS ==

TEMPLATE_CONTEXT_PROCESSORS = (
  # django.core.context_processors.*
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  
  # django.contrib.*
  "django.contrib.auth.context_processors.auth",
  "django.contrib.messages.context_processors.messages",
  "sekizai.context_processors.sekizai",
)


# ============================================================ TEMPLATE ROOT DIRECTORY ==

TEMPLATE_DIRS = (
  os.path.join(PROJECT_DIR, '_templates'),
)


# ============================================================ INSTALLED APPS ==

INSTALLED_APPS = (
  # third-party apps
  'mediagenerator',
  'sekizai',
  
  # django.contrib
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',

  # third-party apps
    
  # admin
  'django.contrib.admin',
  'django.contrib.admindocs',
  
  # third-party apps
  'south',
  
  # custom
  'website',
)


# ============================================================ APP: MEDIAGENERATOR SETTINGS ==

"""

USAGE:

In templates:

{% load media %}
{% include_media 'main.css' %}
{% include_media 'main.css' media='screen,print' %}
<img src="{% media_url 'some/image.png' %}" />

"""

MEDIA_GENERATORS = (
    'mediagenerator.generators.copyfiles.CopyFiles',
    'mediagenerator.generators.bundles.Bundles',
    'mediagenerator.generators.manifest.Manifest',
)

MIDDLEWARE_CLASSES = (
  # third-party middleware
  'mediagenerator.middleware.MediaMiddleware', ) + MIDDLEWARE_CLASSES

MEDIA_DEV_MODE = True
DEV_MEDIA_URL = '/_assets/'
PRODUCTION_MEDIA_URL = '/static/'
IGNORE_APP_MEDIA_DIRS = (
  'static',
)
GLOBAL_MEDIA_DIRS = (
  os.path.join(PROJECT_DIR, '_assets'),
)


# ============================================================ LOGGING SETTINGS ==

LOG_FILE = PROJECT_DIR + '/logs/app.log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'simple',

        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

