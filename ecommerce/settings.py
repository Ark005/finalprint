"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# from dotenv import load_dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# load_dotenv(verbose=True)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
#SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'polymorphic',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth_bootstrap',
    'cart',
    'checkout',
    'products',
    'crispy_forms',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'sorl.thumbnail',
    'whitenoise.runserver_nostatic',
    'django.contrib.admindocs',
    'rest_framework',

    #'allauth.socialaccount.providers.vk',
   #allauth.socialaccount.providers.facebook',
   #'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.google',
  
    
 
    # 'send_email.apps.SendEmailConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
  
]

ROOT_URLCONF = 'ecommerce.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        #'DIRS': [os.path.join(BASE_DIR, os.path.join (BASE_DIR,'templates', 'bootstrap', 'allauth', 'account')),],
        #'DIRS': [os.path.join(BASE_DIR, 'templates', 'bootstrap', 'allauth', 'account'),],
         'DIRS': [os.path.join(BASE_DIR, 'templates')],
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



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    
)

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mynewdb',
        'USER' : 'newuser',
        'PASSWORD' : 'password',
        'HOST' : 'localhost',
        'PORT' : '',


    }

}
"""
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True
gettext = lambda s: s

LOCALE_PATHS = (
    BASE_DIR + 'locale/', )

LANGUAGES = [

    ('ru', 'Russian'),
    ('en', 'English'),
    
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/



STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staic'),os.path.join(BASE_DIR, 'staticfiles')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staic')
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


SITE_ID = 2

LOGIN_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
    

# Stripe API keys

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")

"""

# Настройки почты
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

# Сюда поставить пароль и почту 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = 'none'
"""
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'info@005.ru'
EMAIL_HOST_PASSWORD = 'LizaArt005!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True




DEFAULT_FROM_EMAIL = 'info@005.ru'
DEFAULT_TO_EMAIL = '005ark@gmail.com'


THUMBNAIL_DEBUG = False,



USE_I18N = True # интернационалицация по-умолчанию включена

ACCOUNT_EMAIL_VERIFICATION = 'none'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

#all-auth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 # 1 day. This does ot prevent admin login frombeing brut forced.
ACCOUNT_LOGOUT_REDIRECT_URL ='/' #or any other page
LOGIN_REDIRECT_URL = '/' # redirects to profile page by default
ACCOUNT_PRESERVE_USERNAME_CASING = False # reduces the delays in iexact lookups
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL=True
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_USERNAME_VALIDATORS = None


REST_FRAMEWORK = {
    # Используйте стандартные Django  `django.contrib.auth` разрешения,
    # или разрешите доступ только для чтения для неаутентифицированных пользователей.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


#Account adapters
#ACCOUNT_ADAPTER = 'products.adapter.CustomProcessAdapter'

#Account Signup
#ACCOUNT_FORMS = {'signup': 'products.forms.SignupForm',}

#Social Account Settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
     'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
SOCIALACCOUNT_QUERY_EMAIL=ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_EMAIL_REQUIRED=ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_STORE_TOKENS=False
SOCIAL_AUTH_REDIRECT = True