# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 15:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0006_auto_20160414_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='table', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tablerow',
            name='coefficient',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='tablerow',
            name='point',
            field=models.FloatField(default=0),
        ),
    ]
