# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_press_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='press',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
