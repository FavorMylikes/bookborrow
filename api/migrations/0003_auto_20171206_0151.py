# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-05 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171206_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookuser',
            old_name='book_isbn',
            new_name='isbn',
        ),
    ]
