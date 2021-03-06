# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-30 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20191130_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='acc_now_delinq',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='application_type',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='collection_recovery_fee',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='collections_12_mths_ex_med',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='emp_title',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='initial_list_status',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='mths_since_last_major_derog',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='recoveries',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='tot_coll_amt',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='total_rec_late_fee',
            field=models.CharField(max_length=6),
        ),
    ]
