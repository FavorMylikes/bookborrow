# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/6 1:15
from django.test import TestCase, SimpleTestCase
from unittest import skip, skipIf, SkipTest
from api.models import *
from django.forms.models import model_to_dict
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class ServiceTest(SimpleTestCase):
    def get_openid(self):
        from .services import get_openid
        try:
            data = get_openid(settings.openid)
            self.session_key = data["session_key"]
            logger.info("session_key:%s" % self.session_key)
        except Exception as e:
            logger.exception(e)
            self.session_key = None

    def get_crypt(self):
        from api.WXBizDataCrypt import WXBizDataCrypt

        appId = settings.WX_APP_ID
        # 以下从conf.test 加载
        session_key = settings.session_key
        raw_data = settings.raw_data
        encrypted_data = settings.encrypted_data
        signature = settings.signature
        iv = settings.iv

        pc = WXBizDataCrypt(appId, session_key)
        logger.info(pc.decrypt(encrypted_data, iv))

        from hashlib import sha1

        logger.info(sha1((raw_data + session_key).encode('utf-8')).hexdigest() == signature)

    def test(self):
        self.get_openid()
        self.get_crypt()


@skip("skip ModelTest")
class ModelTest(SimpleTestCase):  # TestCase for db create SimpleTestCase for no db create
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
        user = User.objects.create(**data)

        data = dict()
        data["title"] = "title"
        data["author"] = "author"
        data["translator"] = "translator"
        data["publisher"] = "publisher"
        data["img"] = "img"
        data["rate"] = 3.1
        data["isbn"] = "isbn"

        book = Book.objects.create(**data)
        data = dict()
        data["isbn"] = "isbn"
        data["latitude"] = 3.1
        data["longitude"] = 3.2
        data["altitude"] = 4
        data["vertical_accuracy"] = 0
        data["horizontal_accuracy"] = 0
        data["accuracy"] = 0

        BookUser.objects.create(user=user, book=book, **data)

    def test_models(self):
        print(BookUser.objects.get(isbn="isbn").altitude)
        print(User.objects.get(nick_name="--NULL--").id)

        data = dict()
        data["title"] = "title"
        data["author"] = "author"
        data["translator"] = "translator"
        data["publisher"] = "publisher"
        data["isbn"] = "isbn2"
        book = Book.objects.create(**data)
        data["img"] = "img"
        data["rate"] = 3.1

        print(model_to_dict(book))
        data["isbn"] = "isbn1"
        book = Book.objects.create(**data)
        books = Book.objects.filter(isbn="isbn")
        print(books)
        for book in books:
            print(book)
        print(model_to_dict(book))

    def test_request(self):
        from django.test import Client

        c = Client()
        response = c.get('/api/search/', {"isbn": "9787100012065"})
        for book in Book.objects.all():
            print(model_to_dict(book))
        # print(Book.objects.filter(isbn="9787100012065")[0])
        print(response.status_code)
        print(response.content)
        data = dict()
        data["isbn"] = "9787100012065"
        data["latitude"] = 3.1
        data["longitude"] = 3.2
        data["altitude"] = 4
        data["vertical_accuracy"] = 0
        data["horizontal_accuracy"] = 0
        data["accuracy"] = 0
        data["nick_name"] = "nick_name"
        data["avatar_url"] = "avatar_url"
        data["gender"] = 1
        data["language"] = "language"
        data["country"] = "country"
        data["province"] = "province"
        data["city"] = "city"
        response = c.get('/api/add/', data)
        print(response.status_code)
        print(response.content)
