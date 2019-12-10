# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-13 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TVShows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='releast_date',
            new_name='release_date',
        ),
        migrations.AddField(
            model_name='show',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]