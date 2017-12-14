# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/11/26 1:46

import json, logging, traceback
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.staticfiles.templatetags.staticfiles import static
from api.models import *
from util import url
from django.forms.models import model_to_dict
from api.services import *

logger = logging.getLogger(__name__)


def isbn(request):
    res = dict(title="没找到", author="沃·夏靴德", publisher="找不到出版社",
               img=url.root() + static("image/cover_404.gif"), rate='0',
               translator='')
    try:
        if request.method == 'GET':
            logger.info(request.GET)
            isbn = request.GET["isbn"]
            book = Book.objects.filter(isbn=isbn)
            if len(book) != 0:  # 如果在库里则返回库里的数据
                res.update(model_to_dict(book[0], exclude='create_datetime'))
            else:  # 否则去豆瓣请求数据
                res.update(get_book_douban(isbn))
                if res["title"] != "没找到":
                    Book.objects.create(**res)
            res["nick_name"] = []
            for row in BookUser.objects.filter(isbn=isbn):
                res["nick_name"].append(row.user.nick_name)
    except Exception as e:
        res["nick_name"] = []
        logger.error(e)
    return HttpResponse(json.dumps(res))


def add(request):
    res = dict(success=0)
    if request.method == 'GET':
        logger.info(request.GET)
        try:
            data = dict()
            data["nick_name"] = request.GET.get("nick_name", None)
            data["avatar_url"] = request.GET.get("avatar_url", None)
            data["gender"] = request.GET.get("gender", None)
            data["language"] = request.GET.get("language", None)
            data["country"] = request.GET.get("country", None)
            data["province"] = request.GET.get("province", None)
            data["city"] = request.GET.get("city", None)
            data["open_id"] = request.GET.get("open_id", None)
            try:
                user = User.objects.get(nick_name=data["nick_name"])
                if user.open_id is None or user.open_id == "":
                    user.open_id=data["open_id"]
                    user.save()
            except User.DoesNotExist:
                user = User.objects.create(**data)
            isbn = request.GET.get("isbn", None)
            try:
                book = Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                book = get_book_douban(isbn)
                book = Book.objects.create(**book)
            data.clear()
            data["user"] = user
            data["book"] = book
            data["isbn"] = isbn
            data["latitude"] = request.GET.get("latitude", 0)
            data["longitude"] = request.GET.get("longitude", 0)
            data["altitude"] = request.GET.get("altitude", -1)
            data["vertical_accuracy"] = request.GET.get("vertical_accuracy", -1)
            data["horizontal_accuracy"] = request.GET.get("horizontal_accuracy", -1)
            data["accuracy"] = request.GET.get("accuracy", -1)

            BookUser.objects.create(**data)
            res["success"] = 1
        except Exception as e:
            logger.exception(e)
            res["success"] = 0
            return HttpResponseBadRequest()
    return HttpResponse(json.dumps(res))


def check(request):
    res = {"success": 0}
    if request.method == "GET":
        logger.info(request.GET)
        try:
            code = request.GET["code"]
            encrypted_data = request.GET["encryptedData"]
            raw_data = request.GET["rawData"]
            iv = request.GET["iv"]
            signature = request.GET["signature"]
            res = decrypt(code, encrypted_data, iv, signature,raw_data)
            try:
                user = User.objects.get(nick_name=res["nick_name"])
                if user.open_id is None or user.open_id == "":
                    user.open_id=res["open_id"]
                    user.save()
            except User.DoesNotExist:
                user = User.objects.create(**res)
            res.clear()
            res["success"] = 1
        except Exception as e:
            logger.exception(e)
            return HttpResponseBadRequest()
    return HttpResponse(json.dumps(res))


if __name__ == '__main__':
    print(__name__)
