# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-11-28 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcb_web_auth', '0005_auto_20181128_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddsendpoint',
            name='openid_provider_service_id',
            field=models.CharField(help_text='The Service ID of the OpenID provider registered with data service, required for GET /user/api_token', max_length=64),
        ),
    ]