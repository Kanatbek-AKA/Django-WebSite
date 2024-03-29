"""
Django settings for docean project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DEBUG"]

# wdb | pdb
# DEBUG_PROPOGATE_EXCEPTIONS = True


ALLOWED_HOSTS = ['127.0.0.1']

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_BROWSER_XSS_FILTER = True
#SECURE_HSTS_PRELOAD = True    # 

SESSION_COOKIE_SECURE = True


# LANGUAGE_COOKIE_DOMAIN = None
# CSRF_TRUSTED_ORIGINS = ['https://...host.....app']
# INTERNAL_IPS = []
# CONN_MAX_AGE = 0 # restrict
CONN_HEALTH_CHECKS = True  # improve the robustness of connection

# Application definition
INSTALLED_APPS = [
    "example.apps.ExampleConfig",
    "week1.apps.Week1Config",
    "week2.apps.Week2Config",
    "week3.apps.Week3Config",
    "week4.apps.Week4Config",
    "week5.apps.Week5Config",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_cleanup.apps.CleanupConfig",
    # 'django_pdb',
    # 'django_extensions',
    "component_tags",
    "rest_framework",
    "corsheaders",
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "docean.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "example",
            BASE_DIR / "week2/templates",
            BASE_DIR / "week3",
            BASE_DIR / "week4",
            BASE_DIR / "week5",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


WSGI_APPLICATION = "docean.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# CORS_ALLOWED_ORIGINS = ['https://domain.com', 'https://subdomain.com']
# CORS_ALLOWED_ORIGIN_REGEXES = [r'^https://\w\.domain\.com$', etc...]
# CORS_ALLOW_ALL_ORIGINS = [False]     # True is not allowed
# CORS_ALLOW_METHODS = ['GET', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']
# from corsheaders.defaults import default_methods
# CORS_ALLOW_METHODS = list(default_methods) + ['POKE', 'GET', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']
# CORS_ALLOW_HEADERS = ['accept', 'accept-enconding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with']
# CSRF_TRUSTED_ORIGINS = ['https://get.allowed.dom']
#  more information on the website


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Add  following statics:
# STATICFILES_DIRS tuple tells Django where to look for static files that are not tied to a particular app.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static/templ_css/"),
    os.path.join(BASE_DIR, "static/labs_css/"),
)
# Using the collectstatic command, Django looks for all static files in your apps and collects them wherever you told it to, i.e. the STATIC_ROOT.
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
