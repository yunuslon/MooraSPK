# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-25 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0017_auto_20180924_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-Laki', 'Pria'), ('Perempuan', 'Wanita')], default='Laki-Laki', max_length=2),
        ),
    ]
