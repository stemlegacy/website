# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-19 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20170419_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberss',
            name='email',
            field=models.CharField(default='', max_length=250),
        ),
    ]
