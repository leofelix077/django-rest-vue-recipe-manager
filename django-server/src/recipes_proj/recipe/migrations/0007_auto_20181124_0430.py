# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-24 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20181124_0229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['last_modified'], 'verbose_name': 'recipe', 'verbose_name_plural': 'recipes'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
