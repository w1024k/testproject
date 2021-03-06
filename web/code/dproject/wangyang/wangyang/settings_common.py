# coding=utf-8
"""
Django settings for wangyang project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cgxt57p&xb1*t3ih9&nc9j7k7l33(2bxqsfkvk(00ot63g14^&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'djcelery',
    'common',
    'lm',
    'weixin',
    'cloud',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'common.middleware.message.AdminOnlyMessageMiddleware',
    'common.middleware.visit.VisitCount',
)

ROOT_URLCONF = 'wangyang.urls'

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "OPTIONS": {
            # Match the template names ending in .html but not the ones in the admin folder.
            "match_extension": ".html",
            "match_regex": r"^(?!admin/).*",
            # app里的目录
            "app_dirname": "templates",

            # Can be set to "jinja2.Undefined" or any other subclass.
            "undefined": None,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],

            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ],
            "bytecode_cache": {
                "name": "default",
                "backend": "django_jinja.cache.BytecodeCache",
                "enabled": False,
            },
            "autoescape": True,
            "auto_reload": DEBUG,
            "translation_engine": "django.utils.translation",
        }
    },
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

WSGI_APPLICATION = 'wangyang.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wangyang',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


# #collect目录
# STATIC_ROOT = '/static'

ERROR = {
    'SUCC': {'code': '10000', 'msg': u'成功'},
    'ERROR': {'code': '10001', 'msg': u'未知错误'},
    'PARA_ERR': {'code': '10002', 'msg': u'表单参数错误'},
    'NOT_EXIST_ERR': {'code': '10003', 'msg': u'记录不存在'},
    'PERM_ERR': {'code': '10004', 'msg': u'没有权限进行该操作'},
    'SYS_ERR': {'code': '10005', 'msg': u'系统繁忙'},
    'EXIST_ERR': {'code': '10006', 'msg': u'记录已存在'},
    'FORBIDDEN': {'code': '10007', 'msg': u'被禁止'},
    'MAINTAINANCE': {'code': '10008', 'msg': u'功能维护'},
    'FORBIDDEN_WORD_ERR': {'code': '10010', 'msg': u'内容中包含敏感词'},
    'STATE_ERR': {'code': '10011', 'msg': u'状态错误'},
    'VERIFYCODE_ERR': {'code': '10012', 'msg': u'验证码错误'},
    'OVERFLOW_MAX_LENGTH_ERR': {'code': '10014', 'msg': u'超出内容长度限制'},
    'UNSUPPORT_ERR': {'code': '10016', 'msg': u'不支持该功能'},
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        'TIMEOUT': 60,
        "OPTIONS": {
            "PASSWORD": "redis",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {  # 日志格式
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {  # 过滤器
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {  # 处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {  # 发送邮件通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],  # 仅当 DEBUG = False 时才发送邮件
            'include_html': True,
        },
        'info_handler': {  # 记录到文件
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
            'filters': ['require_debug_false'],
            'formatter': 'standard',
        },
        # 'console': {  # 输出到控制台
        #     'level': 'ERROR',  # 设为debug时,一些数据的查询信息之类的信息都会被打印
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'standard',
        # },
    },
    'loggers': {  # logging管理器
        'django': {
            'handlers': ['info_handler'],
            'level': 'ERROR',
            # 'propagate': False
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}

# 管理员邮箱
ADMINS = (
    ('wangyang', 'w1024k@163.com'),
)

djcelery.setup_loader()

# 非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS
# Email设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465  # SMTP服务端口
EMAIL_HOST_USER = 'wangyangpublic@163.com'  # 我的邮箱帐号
EMAIL_HOST_PASSWORD = 'wangyang001'  # 授权码
EMAIL_USE_TLS = True  # 开启安全链接
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 设置发件人
