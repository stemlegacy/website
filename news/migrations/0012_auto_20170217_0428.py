# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-17 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AddField(
            model_name='gallery',
            name='place',
            field=models.CharField(default='place', max_length=500),
        ),
        migrations.AddField(
            model_name='images',
            name='eventt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.gallery'),
        ),
    ]
