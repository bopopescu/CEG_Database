# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 14:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ceg', '0014_userprofile_userproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='project',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userproject',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
