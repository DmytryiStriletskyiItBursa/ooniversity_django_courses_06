# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Lesson',
        ),
    ]
