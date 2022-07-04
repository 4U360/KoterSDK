"""
Django settings for KoterSdkGRC project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import environ, os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    PHONENUMBER_DB_FORMAT=(str, "E164"),
    PHONENUMBER_DEFAULT_REGION=(str, "BR"),
    PHONENUMBER_DEFAULT_FORMAT=(str, "E164"),
    SECRET_KEY=(str, "CHANGE-THIS-KEY"),
    LANGUAGE_CODE=(str, "pt-br"),
    TIME_ZONE=(str, "America/Sao_Paulo"),
    KOTER_REQUIRE_WORLD_ID=(bool, False),
    KOTER_WORLD_ID_FIELD=(str, "cpf"),
    KOTER_EXTERNAL_USER_MODEL=(str, "KoterSDK.ExternalUser"),
    KOTER_INTEGRATION_ID=(str, None),
    ALLOWED_HOSTS=(list, ["127.0.0.1", '*.4u360.dev.br', '*.4u360.com.br']),
    KOTER_DEFAULT_ALGORITHM=(str, 'HS512'),
    KOTER_SERVER_URL=(str, "koter.4u360.dev.br"),
    KOTER_CLIENT_CERTIFICATE=(str, None),
    KOTER_CLIENT_SECRET=(str, None),
    KOTER_ISSUER=(str, None),
    KOTER_AUDIENCE=(str, None),
    KOTER_SECRET_KEY=(str, ""),
    KOTER_ALGORITHM=(str, None),
    KOTER_SECRET_HEADER=(str, 'Koter-Webhook-Token'),
    KOTER_DELETE_OLD_HOOKS=(bool, False),
    KOTER_DELETE_HOOKS_IN_N_DAYS=(int, 7),
    KOTER_IP_WHITELIST=(list, ["127.0.0.1"])
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'ajax_datatable',
    'rest_framework',
    'reversion',
    "KoterSDK"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'KoterSdkGRC.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'KoterSdkGRC.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = env.str('LANGUAGE_CODE', "pt-br")

TIME_ZONE = env.str("TIME_ZONE")

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Phonenumbers
PHONENUMBER_DB_FORMAT = env.str("PHONENUMBER_DB_FORMAT")
PHONENUMBER_DEFAULT_REGION = env.str("PHONENUMBER_DEFAULT_REGION")
PHONENUMBER_DEFAULT_FORMAT = env.str("PHONENUMBER_DEFAULT_FORMAT")

# Koter

"""
Will user access to view API fields be evaluated?
Attention: Currently, only Brazilian document verification is supported, you can extend the KoterSDK.ExternalUser model
and create your own validation fields and methods.
"""
KOTER_REQUIRE_WORLD_ID = env.bool('KOTER_REQUIRE_WORLD_ID')
KOTER_WORLD_ID_FIELD = env.str('KOTER_WORLD_ID_FIELD')
KOTER_EXTERNAL_USER_MODEL = env.str('KOTER_EXTERNAL_USER_MODEL')
KOTER_INTEGRATION_ID = env.str('KOTER_INTEGRATION_ID')
KOTER_DEFAULT_ALGORITHM = env.str('KOTER_DEFAULT_ALGORITHM')
KOTER_SERVER_URL = env.str('KOTER_SERVER_URL')
KOTER_ISSUER = env.str('KOTER_ISSUER')
KOTER_AUDIENCE = env.str('KOTER_AUDIENCE')
KOTER_EXPIRES = {
    "minutes": 5
}
KOTER_SECRET_KEY = env.str('KOTER_SECRET_KEY')
KOTER_ALGORITHM = env.str('KOTER_ALGORITHM')
KOTER_SECRET_HEADER = env.str('KOTER_SECRET_HEADER')
KOTER_DELETE_OLD_HOOKS = env.bool('KOTER_DELETE_OLD_HOOKS')
KOTER_DELETE_HOOKS_IN_N_DAYS = env.int('KOTER_DELETE_HOOKS_IN_N_DAYS')
KOTER_IP_WHITELIST = env.list('KOTER_IP_WHITELIST')

assert KOTER_ISSUER, """Please configure the communication related variables.
Pending variable: %s""" % "KOTER_ISSUER"
assert KOTER_AUDIENCE, """Please configure the communication related variables.
Pending variable: %s""" % "KOTER_AUDIENCE"

DATA_UPLOAD_MAX_NUMBER_FIELDS = None



# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ]
}
