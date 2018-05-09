# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-01 17:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orb', '0050_auto_20180501_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcefile',
            name='create_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resource_file_create_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resourcefile',
            name='update_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resource_file_update_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
