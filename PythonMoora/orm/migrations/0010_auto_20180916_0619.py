# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-16 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0009_auto_20180916_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademik',
            name='nilai',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='hasiltes',
            name='nilai',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='karakter',
            name='baik',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='karakter',
            name='buruk',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='karakter',
            name='cukup_baik',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='kelas_1',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='kelas_2',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='kelas_3',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='plomba',
            name='cukup_sering',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='plomba',
            name='jarang',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='plomba',
            name='sering',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='plomba',
            name='tidak_pernah',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
    ]