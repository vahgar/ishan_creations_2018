# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('profile', models.CharField(blank=True, max_length=4096, null=True)),
                ('services', models.CharField(blank=True, max_length=4096, null=True)),
                ('timings', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=10, null=True)),
                ('Email', models.EmailField(blank=True, max_length=70, null=True)),
                ('website', models.CharField(max_length=70, default='#')),
                ('social_media', models.CharField(max_length=300, default='#')),
                ('customer_rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
