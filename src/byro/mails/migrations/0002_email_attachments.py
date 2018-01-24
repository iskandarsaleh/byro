# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='attachments',
            field=models.ManyToManyField(related_name='mails', to='documents.Document'),
        ),
    ]