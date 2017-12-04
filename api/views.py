# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/11/26 1:46

import requests, json, logging, traceback
from django.http import HttpResponse
from api.db import *

logger = logging.getLogger(__name__)


def isbn(request):
    try:
        res = {"name": "没找到"}
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
            return HttpResponse(json.dumps(res))
    except Exception as e:
        logger.error(e)


def add(request):
    if request.method == 'GET':
        try:
            data = {}
            data["nick_name"] = request.GET["nick_name"]
            data["avatar_url"] = request.GET["avatar_url"]
            data["gender"] = request.GET["gender"]
            data["language"] = request.GET["language"]
            data["country"] = request.GET["country"]
            data["province"] = request.GET["province"]
            data["city"] = request.GET["city"]
            data["isbn"] = request.GET["isbn"]
            logger.info(request.GET)
            data["latitude"] = request.GET["latitude"]
            data["longitude"] = request.GET["longitude"]
            data["altitude"] = request.GET["altitude"]
            data["vertical_accuracy"] = request.GET.get("vertical_accuracy",-1)
            data["horizontal_accuracy"] = request.GET.get("horizontal_accuracy",-1)
            data["accuracy"] = request.GET.get("accuracy",-1)

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
