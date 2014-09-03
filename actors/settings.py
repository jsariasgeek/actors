"""
Django settings for actors project.

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
SECRET_KEY = 'hip3ek2y*96^5)a!6cnpid$%d!d**+9e)qzu3s7k84(6p6w-=*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Libraries
    'storages',
    'boto',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'actors.urls'

WSGI_APPLICATION = 'actors.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'actors',
            'USER': os.environ['LOCAL_DATABASE_USER'],
            'PASSWORD': os.environ['LOCAL_DATABASE_PASS'],
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    #Heroku Database Settings
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # STATIC_ROOT = 'staticfiles'
    # STATIC_URL = '/static/'

    # STATICFILES_DIRS = (
    #     os.path.join(BASE_DIR, 'static'),
    # )
    
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# HEROKU settings


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

