# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-30 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191130_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='loan_status',
            field=models.CharField(max_length=1),
        ),
    ]