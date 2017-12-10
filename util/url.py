#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/10 10:44

from django.conf import settings
def root():
    return "%(protocol)s://%(host)s/%(app)s" % settings.WEB_CONFIG