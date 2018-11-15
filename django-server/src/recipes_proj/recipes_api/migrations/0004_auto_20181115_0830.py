# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-15 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_api', '0003_auto_20181115_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrecipes',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='userrecipes',
            name='image',
            field=models.TextField(blank=True, max_length=65536),
        ),
        migrations.AlterField(
            model_name='userrecipes',
            name='image_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userrecipes',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]