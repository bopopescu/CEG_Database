# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceg', '0018_userprofile_userproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baud_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Flows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection', models.CharField(default='', max_length=50, unique=True)),
                ('version', models.CharField(default='', max_length=50)),
                ('last_update', models.DateTimeField(verbose_name='date published')),
                ('data_from', models.CharField(default='', max_length=50)),
                ('data_to', models.CharField(default='', max_length=50)),
                ('master_name', models.CharField(default='', max_length=100)),
                ('master_port', models.CharField(default='', max_length=20)),
                ('master_address', models.CharField(default='', max_length=10)),
                ('slave_name', models.CharField(default='', max_length=50)),
                ('slave_port', models.CharField(default='', max_length=20)),
                ('slave_address', models.CharField(default='', max_length=10)),
                ('baud_rate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ceg.Baud_Rate')),
            ],
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='data_flows',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ceg.Project'),
        ),
        migrations.AddField(
            model_name='data_flows',
            name='protocol',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ceg.Protocol'),
        ),
    ]
