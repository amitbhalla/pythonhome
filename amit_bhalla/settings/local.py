"""
Local development settings for amit_bhalla project.
"""
import os
from dotenv import load_dotenv
from .base import *

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-hlvb4e&=8&z85j1l5sdm6nx&u&u^pv%cv7_$3s$xuwfko1p++2")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Override database settings if DATABASE_URL is provided in .env
database_url = os.getenv('DATABASE_URL')
if database_url:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(
        default=database_url,
        conn_max_age=600,
    )

# Disable SSL settings for local development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Development-specific logging
LOGGING['loggers']['django']['level'] = os.getenv('DJANGO_LOG_LEVEL', 'INFO')

# Enable Django Debug Toolbar if installed
if os.getenv('ENABLE_DEBUG_TOOLBAR', 'False') == 'True':
    try:
        import debug_toolbar
        INSTALLED_APPS += ['debug_toolbar']
        MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
        INTERNAL_IPS = ['127.0.0.1']
    except ImportError:
        pass
