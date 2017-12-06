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
        user=User.objects.create(**data)

        data=dict()
        data["title"] = "title"
        data["author"] = "author"
        data["translator"] = "translator"
        data["publisher"] = "publisher"
        data["img"] = "img"
        data["rate"] = 3.1
        data["isbn"] = "isbn"

        book=Book.objects.create(**data)
        data = dict()
        data["isbn"] = "isbn"
        data["latitude"] = 3.1
        data["longitude"] = 3.2
        data["altitude"] = 4
        data["vertical_accuracy"] = 0
        data["horizontal_accuracy"] = 0
        data["accuracy"] = 0

        BookUser.objects.create(user=user,book=book,**data)


    def test_models(self):
        print(BookUser.objects.get(isbn="isbn").altitude)
        print(User.objects.get(nick_name="--NULL--").id)
