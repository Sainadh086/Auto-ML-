# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-09 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20191209_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='addr_state',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='dti',
            field=models.CharField(max_length=5),
        ),
    ]