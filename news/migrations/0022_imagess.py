# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-20 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
            ],
        ),
    ]
