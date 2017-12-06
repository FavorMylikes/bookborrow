# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/12/6 0:05
from django.db import models


class User(models.Model):
    nick_name = models.CharField(max_length=32, null=False)
    avatar_url = models.CharField(max_length=128, null=False)
    gender = models.IntegerField()
    language = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32, default="")


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    translator = models.CharField(max_length=64)
    publisher = models.CharField(max_length=32)
    img = models.CharField(max_length=128)
    rate = models.FloatField(max_length=0)
    isbn = models.CharField(max_length=128, null=False)


class BookUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, unique=True)
    isbn = models.CharField(max_length=64, null=False)
    latitude = models.FloatField(max_length=0, null=False)
    longitude = models.FloatField(max_length=0, null=False)
    altitude = models.IntegerField(null=False)
    vertical_accuracy = models.IntegerField(null=False)
    horizontal_accuracy = models.IntegerField(null=False)
    accuracy = models.IntegerField(null=False)
    create_datetime = models.DateTimeField(auto_created=True,blank=True,null=True)


