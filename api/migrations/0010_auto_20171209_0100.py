# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-08 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171207_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookuser',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
