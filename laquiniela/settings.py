"""
Django settings for laquiniela project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#utf-8
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {var_name} environment variable'
        raise ImproperlyConfigured(error_msg.format(var_name=var_name))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nc+=&l-f5$%+bq3(+==gxly%+urk3_(qcxy3y#sxghwbv=gn1v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(PROJECT_ROOT,'files')


MEDIA_URL = '/media/'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'calendars',
    'teams',
    'footballpools',
    'footballpoolsusers',
    'south',
    'rest_framework',
    'social.apps.django_app.default',
    'main',
    'api',
    'knockout',
    'quarter',
    'semifinal',
    'final',
    'invitations',
    'curiosidades',
    'calendars_knockout',
    'calendars_quarter',
    'calendars_semifinal',
    'calendars_final',   
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'laquiniela.urls'

WSGI_APPLICATION = 'laquiniela.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiniela',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# REST FRAMEWORK




# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    #'main.pipeline.save_profile_picture',
    #'main.pipeline.get_user_avatar',
    #'main.pipeline.get_friends',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

LOGIN_URL = '/'

# API KEY SOCIAL LOGIN


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

SOCIAL_AUTH_RAISE_EXCEPTIONS = True


#TWITTER

SOCIAL_AUTH_TWITTER_KEY = '6FsveoSUgz2s4xamm0IJk7MwG'
SOCIAL_AUTH_TWITTER_SECRET = 'GzN3ejudPZjExtRGy5HTuFwcKZAajzoBV4ds8OeaNyCH1NYyZj'

#FACEBOOK

SOCIAL_AUTH_FACEBOOK_KEY = '826899150657630'
SOCIAL_AUTH_FACEBOOK_SECRET = '5547d055f6be2728b521e48ec2d89c46'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

#SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [('birthday', 'birthday'),('friends','friends'),('picture','picture')]
SOCIAL_AUTH_TWITTER_PROFILE_EXTRA_PARAMS = {'fields':'picture'}

"""SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields':'picture'}
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields':'friends'}
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields':'birthday'}"""

#SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields':'picture','fields' : 'birthday',}

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'
SOCIAL_AUTH_LOGIN_URL = '/login/'

SOCIAL_AUTH_SESSION_EXPIRATION = True

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'williamsnieves@gmail.com'

EMAIL_HOST_PASSWORD = 'ERwilli12345678.'

EMAIL_PORT = 587

