# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/6 1:15
from django.test import TestCase
from api.models import *


class ModelTest(TestCase):
    def setUp(self):
        data = dict()
        request = ModelTest()
        request.GET = {}
        data["nick_name"] = request.GET.get("nick_name", "--NULL--")
        data["avatar_url"] = request.GET.get("avatar_url", "--NULL--")
        data["gender"] = request.GET.get("gender", 0)
        data["language"] = request.GET.get("language", "--NULL--")
        data["country"] = request.GET.get("country", "--NULL--")
        data["province"] = request.GET.get("province", "--NULL--")
        data["city"] = request.GET.get("city", "--NULL--")
        User.objects.create(**data)

    def test_models(self):
        print(User.objects.get(nick_name="--NULL--").id)
