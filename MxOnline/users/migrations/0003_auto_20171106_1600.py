# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图文件地址'),
        ),
    ]