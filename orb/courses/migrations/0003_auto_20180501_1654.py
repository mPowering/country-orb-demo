# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-01 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_reset_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[(b'archived', b'archived'), (b'draft', b'draft'), (b'published', b'published')], default=b'draft', max_length=50),
        ),
    ]
