# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20161102_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='yt_thumbnail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
