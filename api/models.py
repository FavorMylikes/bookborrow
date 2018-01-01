# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/6 0:05
from django.db import models
import django.utils.timezone as timezone


class User(models.Model):
    nick_name = models.CharField(max_length=32, null=False)
    avatar_url = models.CharField(max_length=128, null=False)
    gender = models.IntegerField()
    language = models.CharField(max_length=32, null=True)
    country = models.CharField(max_length=32, null=True)
    province = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=32, null=True)
    phone_number = models.CharField(max_length=32, unique=True, null=True)
    create_datetime = models.DateTimeField(default=timezone.now, null=True)
    open_id = models.CharField(max_length=28, null=True)


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    translator = models.CharField(max_length=64, null=True)
    publisher = models.CharField(max_length=32, null=True)
    img = models.CharField(max_length=128)
    rate = models.FloatField(max_length=0, null=True)
    isbn = models.CharField(max_length=128, null=False, unique=True)
    create_datetime = models.DateTimeField(default=timezone.now, null=True)


class BookUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=64, null=False)
    latitude = models.FloatField(max_length=0, null=False)
    longitude = models.FloatField(max_length=0, null=False)
    altitude = models.IntegerField(null=False)
    vertical_accuracy = models.IntegerField(null=False)
    horizontal_accuracy = models.IntegerField(null=False)
    accuracy = models.IntegerField(null=False)
    create_datetime = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        unique_together = ('book', 'user',)


# 关注者关注了被关注者
class FollowRelations(models.Model):
    follower = models.ForeignKey(User, related_name="follower", on_delete=models.SET_NULL, null=True)  # 关注者
    followee = models.ForeignKey(User, related_name="followee", on_delete=models.SET_NULL, null=True)  # 被关注者
    create_datetime = models.DateTimeField(default=timezone.now, null=True)


class Article(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    like_count = models.IntegerField(null=True, default=0)
    content = models.TextField(max_length=512)  # 书评正文
    create_datetime = models.DateTimeField(default=timezone.now, null=True)


class Comment(models.Model):  # 对文章的评论表
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    article = models.OneToOneField(Article, on_delete=models.SET_NULL, null=True)
    replay = models.CharField(max_length=128, null=True)  # 应该以4->1，2，3的形式减少遍历次数
    like_count = models.IntegerField(null=True, default=0)
    content = models.TextField(max_length=512)  # 书评正文
    create_datetime = models.DateTimeField(default=timezone.now, null=True)
