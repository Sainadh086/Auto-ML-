# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-10 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_labelname'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelname',
            name='Preprocess',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labelname',
            name='split',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
