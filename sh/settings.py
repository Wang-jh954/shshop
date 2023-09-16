"""
Django settings for sh project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#($0@z-)#&skc_qm-%p17b_isl8t+64q2%z6bd$c)h^h=)l2%+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    #  'letsencrypt',
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.sitemaps",
    "shshop.apps.ShshopConfig",
    "rest_framework",
    "videos",
    "rest_framework.authtoken",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sh.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sh.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sh",  # 数据库名字
        # 'NAME': "se",  # 数据库名字
        "USER": "se",  # 用户名
        # "PASSWORD":"123456",
        "PASSWORD": "bhshm418",
        "HOST": "localhost",  # ip
        "PORT": "3306",
    }
}

# Password validationgit
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

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Default primary key field type
# https://docs.djangoproject.com/zh-hans/4.1/topics/cache/
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# 站点框架 site
# https://docs.djangoproject.com/zh-hans/4.1/ref/contrib/sites/#module-django.contrib.sites
SITE_ID = 1

# 邮箱发送后端配置
# https://docs.djangoproject.com/zh-hans/4.1/topics/email/
EMAIL_HOST = "smtp.qq.com"  # 用于发送电子邮件的主机。
EMAIL_HOST_USER = "robertcjy@qq.com"  # 自己的邮箱地址
EMAIL_HOST_PASSWORD = "xxxxxxx"  # 自己的邮箱密码，或授权码，一般现在的邮箱都需要授权码
EMAIL_PORT = 465  # 用于中定义的SMTP服务器的端口
EMAIL_USE_SSL = True  # 是否使用隐式的安全连接

# 邮件控制台后端
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# 邮件测试后端
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECURE_CROSS_ORIGIN_OPENER_POLICY = "None"


REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.AutoSchema"}

SIMPLEUI_DEFAULT_THEME = "e-purple-pro.css"
SIMPLEUI_HOME_INFO = False
SIMPLEUI_LOGO = "/media/logo.png"
