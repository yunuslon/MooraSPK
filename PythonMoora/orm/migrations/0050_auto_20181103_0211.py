# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-03 02:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orm', '0049_auto_20181101_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='siswa',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orm.User'),
        ),
        migrations.AlterField(
            model_name='siswa_f',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orm.User'),
        ),
        migrations.AlterField(
            model_name='siswa_k',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orm.User'),
        ),
        migrations.AlterField(
            model_name='siswa_m',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orm.User'),
        ),
    ]