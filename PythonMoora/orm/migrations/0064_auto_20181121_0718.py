# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-21 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0063_auto_20181121_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesolimpiade',
            name='no',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]
