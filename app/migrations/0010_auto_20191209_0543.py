# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-09 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191130_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='application_type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='emp_title',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='tot_coll_amt',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='verification_status',
            field=models.CharField(max_length=1),
        ),
    ]
