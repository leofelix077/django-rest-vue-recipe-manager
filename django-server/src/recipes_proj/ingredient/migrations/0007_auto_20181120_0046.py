# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0006_auto_20181120_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='article_number',
            field=models.TextField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
    ]