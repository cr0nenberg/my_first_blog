# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eintrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('betriebsstelle', models.CharField(max_length=200)),
                ('lsz', models.CharField(max_length=200)),
                ('ordnr', models.CharField(max_length=200)),
                ('nkz', models.CharField(max_length=200)),
                ('datum', models.DateTimeField(default=django.utils.timezone.now)),
                ('eintrag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eintraege', to='blog.Post')),
            ],
        ),
    ]
