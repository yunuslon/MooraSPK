# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-29 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0021_auto_20180929_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matematika',
            name='nilai',
            field=models.IntegerField(default=0),
        ),
    ]