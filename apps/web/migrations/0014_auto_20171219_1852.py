# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 18:52
from __future__ import unicode_literals

import apps.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20171213_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='keyboard',
            field=models.TextField(blank=True, max_length=2000, null=True, validators=[apps.web.validators.jinja2_template], verbose_name='Keyboard layout'),
        ),
        migrations.AlterField(
            model_name='response',
            name='message',
            field=models.TextField(blank=True, max_length=5000, null=True, validators=[apps.web.validators.jinja2_template], verbose_name='Message text'),
        ),
    ]