import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_DIR = environ.Path(__file__) - 4
env = environ.Env()

env.read_env(ROOT_DIR(".env"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", bool)
# DEBUG = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS", list)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

EXTERNAL_APPS = [
    'debug_toolbar',
    'jazzmin',
    'django_ckeditor_5',
    'django_celery_beat',
]

OWN_APPS = [
    'fapp',
    'useri',
]
INSTALLED_APPS = EXTERNAL_APPS + OWN_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'core.context_processors.main_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
DATABASES = {
    "default": env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(os.path.join(ROOT_DIR, 'src'), 'static'),
]
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.join(ROOT_DIR, 'src'), 'staticfiles')
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.join(ROOT_DIR, 'src'), 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# настройки кэширования
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/"

# настройки для Celery
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

if DEBUG:
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
    }
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        "versionCheck": False,
        'skin': 'moono',
        'codeSnippet_them': 'monokai',
        'toolbar': 'all',
        'language': 'ru',
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'widget',
                'dialog',
            ]
        ),
    }
}

JAZZMIN_SETTINGS = {
    "site_title": "Demo",
    "site_header": "Demo",
    "site_brand": "Demo",
    "site_icon": "admin_login.png",
    "login_logo": "admin_login.png",
    # Add your own branding here
    "site_logo": "admin_login.png",
    "welcome_sign": "Добро пожаловать на Demo",
    "site_logo_classes": "img",
    # Copyright on the footer
    "copyright": "Demo",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Demo", "url": "home", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    "hide_models": ['store.ProductAttribute',
                    'store.Unit',
                    'store.Price',
                    'store.Vendor',
                    'store.CatAttribute',
                    'store.FilterAttribute',
                    'store.Warehouse',
                    'store.AttributeGroup',
                    'store.Total',
                    'store.ParamName',
                    # 'sites.Site',
                    'PeriodicTask'],
    "order_with_respect_to": ["store", "blog", "settings"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    "custom_css": "admin/css/custome.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
DISPLAY_NAME = env("DISPLAY_NAME")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_USE_SSL = env("EMAIL_USE_SSL")

# # HTTPS settings
# SESSION_COOKIE_SECURE = env("SESSION_COOKIE_SECURE", True)
# CSRF_COOKIE_SECURE = env("CSRF_COOKIE_SECURE", True)
# SECCURE_SSL_REDIRECT = env("SECCURE_SSL_REDIRECT", True)
#
#
# # HSTS settings (HTTP STRIKT TRANSPORT  SECURITY) - ЭТО ГОВОРИТСЯ О ТОМ, ЧТО БРАУЗЕРЫ НЕ МОГУТ ПОДКЛЮЧАТЬСЯ К САЙТУ ЧЕРЕЗ HTTP
# SECURE_HSTS_SECONDS = 31536000 # 1 YEAR
# SECURE_HSTS_PRELOAD = env("SECURE_HSTS_PRELOAD", True)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
