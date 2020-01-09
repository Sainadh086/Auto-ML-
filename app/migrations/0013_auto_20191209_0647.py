# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-09 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20191209_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='annual_inc',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='collection_recovery_fee',
            field=models.CharField(max_length=19),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='emp_length',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='emp_title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='funded_amnt',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='funded_amnt_inv',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='home_ownership',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='loan_amnt',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='member_id',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='mths_since_last_delinq',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='mths_since_last_record',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='open_acc',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='pub_rec',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='purpose',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='revol_bal',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='revol_util',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='term',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='tot_coll_amt',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='tot_cur_bal',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='total_acc',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='total_rec_int',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='total_rec_late_fee',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='total_rev_hi_lim',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='verification_status_joint',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]