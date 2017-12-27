# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_auto_20171218_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='business_entity',
            name='category',
            field=models.ForeignKey(to='entity.Category', null=True, blank=True),
        ),
    ]
