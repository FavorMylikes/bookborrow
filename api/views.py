# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/11/26 1:46

import requests, json, logging, traceback
from django.http import HttpResponse
from api.db import *
from django.conf import settings

logger = logging.getLogger(__name__)


def isbn(request):
    res = dict(name="没找到", author="沃·夏靴德", publisher="找不到出版社",
               img="%(protocol)s://favormylikes/bookborrow/static/image/cover_404.gif" % dict(
                   protocol=settings.WEB_PROTOCOL))
    try:
        if request.method == 'GET':
            isbn = request.GET["isbn"]
            url = "https://api.douban.com/v2/book/isbn/:%s" % isbn
            context = requests.get(url).text
            context = json.loads(context)
            res["name"] = context["title"]
            res["author"] = ",".join(context["author"])
            res["translator"] = ",".join(context["translator"])
            res["publisher"] = context["publisher"]
            res["img"] = None or context["images"]["large"] or context["images"]["medium"] or context["images"]["small"]
            res["rate"] = context["rating"]["average"]
            res["nick_name"] = db_query_isbn(isbn)
    except Exception as e:
        logger.error(e)
    return HttpResponse(json.dumps(res))


def add(request):
    if request.method == 'GET':
        logger.info(request.GET)
        try:
            data = dict()
            data["nick_name"] = request.GET("nick_name", "--NULL--")
            data["avatar_url"] = request.GET("avatar_url", "--NULL--")
            data["gender"] = request.GET("gender", "--NULL--")
            data["language"] = request.GET("language", "--NULL--")
            data["country"] = request.GET("country", "--NULL--")
            data["province"] = request.GET("province", "--NULL--")
            data["city"] = request.GET("city", "--NULL--")
            data["isbn"] = request.GET("isbn", "--NULL--")

            data["latitude"] = request.GET("latitude", 0)
            data["longitude"] = request.GET("longitude", 0)
            data["altitude"] = request.GET("altitude", 0)
            data["vertical_accuracy"] = request.GET.get("vertical_accuracy", -1)
            data["horizontal_accuracy"] = request.GET.get("horizontal_accuracy", -1)
            data["accuracy"] = request.GET.get("accuracy", -1)

            # 获取用户id
            user_id = db_query_userinfo(data["nick_name"])
            if not user_id:
                user_id = db_add_userinfo(data)
            data["user_id"] = user_id or -1
            db_add_book_user(data)
            return HttpResponse(json.dumps({"success": 1}))
        except Exception as e:
            logger.error("".join(traceback.format_tb(e.__traceback__)))
            return HttpResponse(json.dumps({"success": 0}))


if __name__ == '__main__':
    print(__name__)
