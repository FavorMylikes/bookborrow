#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/8 0:27

STATIC_ROOT = '/opt/mylikes/bookborrow/static'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_bookborrow",
        "USER": "root",
        "PASSWORD": "minefield32",
        "HOST": "120.27.96.175",
        "PORT": "3306"
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#web config
PROTOCOL = "https"
HOST = "faovrmylikes.com"
PROJECT = "bookborrow"