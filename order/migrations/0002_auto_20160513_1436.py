# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='service.Service'),
        ),
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masters', to=settings.AUTH_USER_MODEL),
        ),
    ]
