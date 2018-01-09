# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 04:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_auto_20170622_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_valid', models.BooleanField(default=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Feed', to='home.Feeds')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
