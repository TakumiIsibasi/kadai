import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-h@s8+8jo642*hworvaj+6%nfccs8(+$!#xr019u4k2fesdzmy9'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'post.apps.PostConfig',
    'user.apps.UserConfig',
    'mail.apps.MailConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'blogsite.urls'

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

WSGI_APPLICATION = 'blogsite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# STATIC_URLの値を修正
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# メディアファイルの設定を追加
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_AUTO_FIELDを修正
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODELを追加
AUTH_USER_MODEL = 'user.CustomUser'

EMAIL_HOST = 'smtp-mail.outlook.com' # 大原のメールサーバー
EMAIL_PORT = 587 # 大原の設定値

# 各自が stu の MicrosoftAccount に設定しているパスワード
EMAIL_HOST_PASSWORD = '39SuKinn'

# 各自が stu の メールアドレス
DEFAULT_FROM_EMAIL = 'fko2347037@stu.O-hara.ac.jp'
EMAIL_HOST_USER = 'fko2347037@stu.O-hara.ac.jp'

# これは固定でTrue
EMAIL_USE_TLS = True