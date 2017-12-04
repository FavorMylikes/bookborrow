# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/11/26 16:18

import pymysql


def get_connect():
    return pymysql.connect(host='120.27.96.175', port=3306, user='root', passwd='minefield32', db='bookborrow',
                           charset='utf8')


def db_query_isbn(isbn):
    con = get_connect()
    cur = con.cursor()
    query_sql = "select nick_name from book_user join user_info on book_user.user_id = user_info.id where isbn=%(isbn)s;"
    condition = {"isbn": isbn}
    cur.execute(query_sql, condition)
    res = []
    for row in cur.fetchall():
        res.append(row[0])
    cur.close()
    con.close()
    return res


def db_add_userinfo(data):
    con = get_connect()
    cur = con.cursor()
    save_sql = """INSERT
    INTO
    `bookborrow`.
    `user_info`(`nick_name`, `avatar_url`, `gender`, `language`, `country`, `province`, `city`)
    VALUES(%(nick_name)s,%(avatar_url)s,%(gender)s,%(language)s,%(country)s,%(province)s,%(city)s);"""
    cur.execute(save_sql, data)
    user_id = cur.lastrowid
    con.commit()
    cur.close()
    con.close()
    return user_id

def db_query_userinfo(nick_name):
    con = get_connect()
    cur = con.cursor()
    save_sql = """SELECT `id` FROM `user_info` WHERE `nick_name`=%(nick_name)s;"""
    cur.execute(save_sql, {"nick_name":nick_name})
    user_id = None
    for row in cur.fetchall():
        user_id = row[0]
    cur.close()
    con.close()
    return user_id

def db_query_book_number(nick_name):
    con = get_connect()
    cur = con.cursor()
    save_sql = """SELECT COUNT("*") FROM `book_user` join `user_info` on `book_user`.user_id=`user_info`.id WHERE `nick_name`=%(nick_name)s;"""
    data={}
    data["nick_name"]=nick_name
    cur.execute(save_sql, {"nick_name": nick_name})
    row = cur.fetchone()
    res = (row and row[0]) or 0
    cur.close()
    con.close()
    return res

def db_add_book_user(data):
    con = get_connect()
    cur = con.cursor()
    save_sql = """INSERT INTO `bookborrow`.`book_user` (`isbn`, `user_id`,  `latitude`, `longitude`, `altitude`, `vertical_accuracy`, `horizontal_accuracy`, `accuracy`) 
VALUES (%(isbn)s,%(user_id)s,%(latitude)s,%(longitude)s,%(altitude)s,%(vertical_accuracy)s,%(horizontal_accuracy)s,%(accuracy)s
);"""
    cur.execute(save_sql, data)
    res_id = cur.lastrowid
    con.commit()
    cur.close()
    con.close()
    return res_id


if __name__ == '__main__':
    data = {}
    data["nick_name"] = "nick_name"
    data["avatar_url"] = "avatar_url"
    data["gender"] = 1
    data["language"] = "language"
    data["country"] = "country"
    data["province"] = "province"
    data["city"] = "city"

    data["isbn"] = "isbn"
    data["user_id"] = 1
    data["latitude"] = 0.1
    data["longitude"] = 0.2
    data["altitude"] = 3


    nick_name="最爱麦丽素"

    print(db_add_book_user(data))
