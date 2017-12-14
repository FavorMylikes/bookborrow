# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/7 1:10
import requests, json, logging

logger = logging.getLogger(__name__)

from django.conf import settings


def get_book_douban(isbn):
    res = dict()
    try:
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
    except Exception as e:
        logger.exception(e)
    return res


def get_openid(code):
    try:
        app_id = settings.WX_APP_ID
        secret_id = settings.WX_SECRET_ID
        data = {
            "app_id": app_id,
            "secret_id": secret_id,
            "code": code
        }
        url = """https://api.weixin.qq.com/sns/jscode2session?appid=%(app_id)s&secret=%(secret_id)s&js_code=%(code)s&grant_type=authorization_code""" % data
        context = requests.get(url).text
        context = json.loads(context)
        return context
    except Exception as e:
        logger.exception(e)


# 详见文档
# https://mp.weixin.qq.com/debug/wxadoc/dev/api/open.html
# https://mp.weixin.qq.com/debug/wxadoc/dev/api/signature.html
def decrypt(code, encrypted_data, iv, signature, raw_data):
    from api.WXBizDataCrypt import WXBizDataCrypt
    from hashlib import sha1
    app_id = settings.WX_APP_ID
    code = get_openid(code)
    session_key = code["session_key"]
    pc = WXBizDataCrypt(app_id, session_key)
    data = pc.decrypt(encrypted_data, iv)
    data["check"] = sha1((raw_data + session_key).encode('utf-8')).hexdigest() == signature
    res=[]
    res["nick_name"] = data.get("nickame", None)
    res["avatar_url"] = data.get("avatarUrl", None)
    res["gender"] = data.get("gender", None)
    res["language"] = data.get("language", None)
    res["country"] = data.get("country", None)
    res["province"] = data.get("province", None)
    res["city"] = data.get("city", None)
    res["open_id"] = data.get("openId", None)
    logger.info(res)
    return res
