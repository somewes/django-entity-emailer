# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-09-19 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('entity_emailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='view_uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]