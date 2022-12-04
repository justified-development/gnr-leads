"""
Django settings for gnr_leads project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.mail import send_mail
import os.path  

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q$hw_5@u217jn1*by24_#0b8&vp*fr(p)85-1*-+woina@9_gu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'leads.apps.LeadsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    ]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gnr_leads.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/leads/templates/',],
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

WSGI_APPLICATION = 'gnr_leads.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True

# DO NOT commit these fields, for security purposes. If needed, fill them out for testing, and leave them uncommitted
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_RECIPIENT = ''
SCRAPER_LOGIN_URL = ''
SCRAPER_LEADS_URL = ''
# END DO NOT COMMIT

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
TIME_ZONE = 'America/Chicago'

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    IS_PROD=(bool, False)
)

IS_PROD = env('IS_PROD')
if IS_PROD:
    # False if not in os.environ
    DEBUG = env('DEBUG')

    # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
    SECRET_KEY = env('SECRET_KEY')

    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

    EMAIL_HOST_USER = env('EMAIL_HOST_USER')

    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

    EMAIL_RECIPIENT = env('EMAIL_RECIPIENT')

    SCRAPER_LOGIN_URL = env('SCRAPER_LOGIN_URL')

    SCRAPER_LEADS_URL = env('SCRAPER_LEADS_URL')

    # Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
    DATABASES = {
        'default': {
            'ENGINE': 'django_psdb_engine',
            'NAME': env('DB_NAME'),
            'HOST': 'us-east.connect.psdb.cloud',
            'PORT': 3306,
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASS'),
            'OPTIONS': {'ssl': {'ca': '/etc/ssl/certs/ca-certificates.crt'}}
            # 'OPTIONS': {'ssl': {'ca': 'C:\\Users\\bwrig\\Desktop\\curl-ca-bundle.crt'}}
        }
    }