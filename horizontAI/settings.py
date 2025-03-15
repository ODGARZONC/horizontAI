"""
Django settings for horizontAI project.

Generated by 'django-admin startproject'.

For more information, see:
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
import pymysql
pymysql.install_as_MySQLdb()


# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vd%5fve$$gju+zgwa5qe3kl%@o%_bb_u*-adw696&5ez8)u-os'

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Actualiza con los hosts permitidos

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # app personalizada
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'horizontAI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ruta personalizada para plantillas
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

WSGI_APPLICATION = 'horizontAI.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'horizontai',
        'USER': 'odgarzc',
        'PASSWORD': 'r3dJ2jgrT8sU6H%vvc*CNwJZA58Pcf3gCU#F!&YU&WHAs8A2Z1Vsyh%H1eM$GChh',
        'HOST': '127.0.0.1',  # O el host de tu servidor MySQL
        'PORT': '3306',       # Puerto predeterminado de MySQL
    }
   # 'sqlite': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / "horizontAI.db",  # Base de datos SQLite
   # }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend', 'public', 'build', 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Django REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# CORS Settings for React frontend
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# SimpleJWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'ISSUER': 'http://127.0.0.1:8000/',  # Ajusta según tu servidor de producción
}

# Si quieres permitir todas las solicitudes (solo para desarrollo):
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_HEADERS = [
    'Authorization',
    'Content-Type',
    'X-CSRFToken',
]

PORT = os.environ.get('PORT', '8000')  # Predeterminado: 8000 si no se define