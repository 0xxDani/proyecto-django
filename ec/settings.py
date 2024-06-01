from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SE CAMBIA AL SECRET K PARA INICIALIZAR VARIABLE DE ENTORNO EN RENDER.COM
SECRET_KEY = SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = [] #ASTERISCO ENTRE COMILLAS PARA USAR EL NGROK CON PAYPAL Y QUE PERMITA TODOS LOS HOSTS
                   #POR SI ALGÚN PROBLEMA

 # SE CONTROLAN LOS ERRORES DEL USUARIO DE LA VARIABLE DEBUG Y SI LA VARIABLE DETECTA PRODUCCIÓN
 # EL ESTADO PASA A FALSE Y VICEVERSA
 # (VER PASO 8 EN ARCHVIO comandosrutas.txt)

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'paypal.standard.ipn', #IPN PAYPAL
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ec.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ec.wsgi.application'

#SE CAMBIA A BASE DE DATOS POSTGRES PARA PRODUCCIÓN
#VER DOCS: 🩴👉 https://docs.render.com/deploy-django


DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:postgres@localhost/postgres',
        conn_max_age=600  
    )
}


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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-es'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
LOGIN_REDIRECT_URL = '/profile/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#PAGOS
RAZOR_KEY_ID = 'rzp_test_V3NdXPh72wKeN8'
RAZOR_KEY_SECRET = 'VBaWeeL4qat7tGO9Dg6Wk9PF'

PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = 'sb-qzv0529127780@business.example.com'