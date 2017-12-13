# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/14 2:34

from .settings import *


# 测试时指定此文件为test settings 可以跳过migration 的数据库创建
class DisableMigrations(dict):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

DATABASES = DisableMigrations()

MIGRATION_MODULES = DisableMigrations()
