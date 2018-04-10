# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-04-10 16:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gcb_web_auth', '0003_groupmanagerconnection'),
    ]

    operations = [
        migrations.CreateModel(
            name='DDSEndpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('agent_key', models.CharField(max_length=32, unique=True)),
                ('api_root', models.URLField(help_text='Base API URL for data service instance, e.g. https://api.dataservice.duke.edu/api/v1')),
                ('portal_root', models.URLField(verbose_name='Base Web URL for data service isntance, e.g. https://dataservice.duke.edu')),
                ('openid_provider_id', models.CharField(help_text='The Provider ID of the OpenID provider registered with data service', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='DDSUserCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32, unique=True)),
                ('dds_id', models.CharField(max_length=255, unique=True)),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gcb_web_auth.DDSEndpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DukeDSSettings',
        ),
        migrations.AlterUniqueTogether(
            name='ddsusercredential',
            unique_together=set([('endpoint', 'user')]),
        ),
    ]
