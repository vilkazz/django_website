# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='contact_first_line',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='settings',
            name='contact_second_line',
            field=models.TextField(default='', max_length=100),
        ),
    ]
