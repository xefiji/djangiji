"""
Django settings for djangiji project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q9&9%%5=g#x(=eop-@rx6v$u^&s(qfhecct7k(4*echx3%m64r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ADMINS=(
    ('FX Echappe','fxechappe@gmail.com')
)

MAIL_FROM='xefiji <xefiji@62-210-237-46.online.net>'

LOGIN_URL = 'login/'

TEMPLATE_DIRS = (
  "/home/xefiji/django/djangiji/templates",
  # "/home/xefiji/django/djangiji/templates/portfolio",
  "/home/xefiji/django/djangiji/templates/todo",
)

APPEND_SLASH = True  # Ajoute un slash en fin d'URL

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.staticfiles',
    # 'portfolio',
    'todo'
)

TEMPLATE_STRING_IF_INVALID ="[***]"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangiji.urls'

WSGI_APPLICATION = 'djangiji.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo',
        'USER': 'root',
        'PASSWORD': 'glopglop',
        'HOST': 'localhost'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '62.210.237.46:11211',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'fr-FR'

USE_I18N = True

USE_L10N = True

# USE_TZ = True # Commented otherwise store last_login with 1 hour less


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/assets/'

STATICFILES_DIRS = (
    "/home/xefiji/django/djangiji/assets",
)
