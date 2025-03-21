"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@x1+#um=)w*n9*b8f5#f^b5s(vkbwsqz7t+v92+ed4k-4ps%!c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Security settings
SECURE_BROWSER_XSS_FILTER = True  # Protects against XSS
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents content sniffing

# Ensure HTTPS for cookies (only enable in production with HTTPS)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Set a strict Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'",)

# Allowed hosts (change this based on your deployment)
ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1']

# Use environment variables for sensitive data
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'advanced_features_and_security',
     'csp', 
]
AUTH_USER_MODEL = 'advanced_features_and_security.CustomUser'
# Specify the custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  
    # Apply CSP settings
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.message.CommonMiddleware',
    'csp.middleware.CSPMiddleware',
    
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# Enable CSP to prevent XSS attacks
CSP_DEFAULT_SRC = ("'self'",)  # Allow content only from the same origin
CSP_SCRIPT_SRC = ("'self'", "https://trusted-scripts.example.com")  # Allow scripts only from trusted sources
CSP_STYLE_SRC = ("'self'", "https://trusted-styles.example.com")  # Allow styles only from trusted sources
CSP_IMG_SRC = ("'self'", "https://trusted-images.example.com")  # Allow images from trusted sources
CSP_FONT_SRC = ("'self'", "https://trusted-fonts.example.com")  # Allow fonts from trusted sources
CSP_FRAME_ANCESTORS = ("'none'",)  # Prevent the site from being embedded in an iframe

# Prevent clickjacking attacks
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME-type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser's built-in XSS filtering
SECURE_BROWSER_XSS_FILTER = True
# Ensure Django recognizes the HTTP_X_FORWARDED_PROTO header for SSL
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Use HTTP Strict Transport Security (HSTS) to force HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
