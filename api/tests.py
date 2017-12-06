# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/6 1:15
from django.test import TestCase
from api.models import *
from django.forms.models import model_to_dict
import logging

logger = logging.getLogger(__name__)
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
        books=Book.objects.filter(isbn="isbn")
        print(books)
        for book in books:
            print(book)
        print(model_to_dict(book))

    def test_request(self):
        from django.test import Client

        c = Client()
        response = c.get('/api/search/', {"isbn":"9787100012065"})
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
        data["nick_name"] ="nick_name"
        data["avatar_url"] ="avatar_url"
        data["gender"] =1
        data["language"] ="language"
        data["country"] ="country"
        data["province"] ="province"
        data["city"] = "city"
        response = c.get('/api/add/', data)
        print(response.status_code)
        print(response.content)