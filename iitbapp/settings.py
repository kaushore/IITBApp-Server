"""
Django settings for iitbapp project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import settings_user as config
import logging.config
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j^-q6b9j#b527w8t&k_r&a6#j!ot2105yk0yemd*#27%oizw_f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = 'login_page'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'gcm',
    'authentication',
    'news',
    'event',
    'notice',
    'information',
    'content',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'iitbapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'iitbapp/templates'),
            os.path.join(BASE_DIR, 'content/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iitbapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if config.IS_TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'iitbapp.db',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config.DB_ENGINE,
            'NAME': config.DB_NAME,
            'USER': config.DB_USER,
            'PASSWORD': config.DB_PASSWORD,
            'HOST': config.DB_HOST,
            'PORT': config.DB_PORT,
        }
    }

ADMINS = (
    ('Dheerendra Rathor', 'dheeru.rathor14@gmail.com'),
    )

MANAGERS = ADMINS

MEDIA_ROOT = os.path.join(BASE_DIR, 'iitbapp/media/')

STATIC_ROOT = os.path.join(BASE_DIR, 'iitbapp/staticfiles/')

STATICFILES_DIRS = (
    # Add all static files here. use os.path.join(BASE_DIR, 'your/staticfile/path')
    os.path.join(BASE_DIR, 'iitbapp/static'),
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] [%(name)s] [%(module)s] [Process:%(process)d] '
                      '[Thread:%(thread)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file_django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose'
            },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/application.log',
            'formatter': 'verbose'
            },
        },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            },
        'django': {
            'handlers': ['file_django'],
            'level': 'INFO',
            'propagate': False,
            },
        },

    }
logging.config.dictConfig(LOGGING)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}

# User specific settings
EMAIL_HOST = config.EMAIL_HOST
EMAIL_PORT = config.EMAIL_PORT

EMAIL_FROM = config.EMAIL_FROM

EMAIL_USERNAME = config.EMAIL_USERNAME
EMAIL_PASSWORD = config.EMAIL_PASSWORD

ALLOWED_DOMAINS = config.ALLOWED_DOMAINS

GCM_APIKEY = config.GCM_KEY

MEDIA_URL = config.MEDIA_URL

STATIC_URL = config.STATIC_URL

SESSION_COOKIE_PATH = config.SESSION_COOKIE_PATH

CSRF_COOKIE_PATH = config.CSRF_COOKIE_PATH
