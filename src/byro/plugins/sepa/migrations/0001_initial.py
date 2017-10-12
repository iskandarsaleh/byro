# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 20:18
from __future__ import unicode_literals

import byro.common.models.auditable
from django.db import migrations, models
import localflavor.generic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberIban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iban', localflavor.generic.models.IBANField(blank=True, include_countries=None, max_length=34, null=True, use_nordea_extensions=False, verbose_name='IBAN')),
                ('bic', localflavor.generic.models.BICField(blank=True, max_length=11, null=True, verbose_name='BIC')),
                ('institute', models.CharField(blank=True, max_length=255, null=True, verbose_name='IBAN Institute')),
                ('issue_date', models.DateField(blank=True, help_text='The issue date of the direct debit mandate. (1970-01-01 means there is no issue date in the database )', null=True, verbose_name='IBAN Issue Date')),
                ('fullname', models.CharField(blank=True, help_text='Full name for IBAN account owner', max_length=255, null=True, verbose_name='IBAN full name')),
                ('address', models.CharField(blank=True, help_text='Address line (e.g. Street / House Number)', max_length=255, null=True, verbose_name='IBAN address')),
                ('zip_code', models.CharField(blank=True, help_text='ZIP Code', max_length=20, null=True, verbose_name='IBAN zip code')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='IBAN City')),
                ('country', models.CharField(blank=True, default='Deutschland', max_length=255, null=True, verbose_name='IBAN Country')),
                ('mandate_reference', models.CharField(blank=True, max_length=255, null=True, verbose_name='IBAN Mandate Reference')),
                ('mandate_reason', models.CharField(blank=True, max_length=255, null=True, verbose_name='IBAN Mandate Reason')),
            ],
            bases=(byro.common.models.auditable.Auditable, models.Model),
        ),
    ]
