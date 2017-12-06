# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/7 1:10
import requests, json


def get_book_douban(isbn):
    res = dict()
    url = "https://api.douban.com/v2/book/isbn/:%s" % isbn
    context = requests.get(url).text
    context = json.loads(context)
    res["title"] = context["title"]
    res["author"] = ",".join(context["author"])
    res["translator"] = ",".join(context["translator"])
    res["publisher"] = context["publisher"]
    res["img"] = None or context["images"]["large"] or context["images"]["medium"] or context["images"][
        "small"]
    res["rate"] = context["rating"]["average"]
    res["isbn"] = isbn
    return res