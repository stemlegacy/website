# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-19 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20170420_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
