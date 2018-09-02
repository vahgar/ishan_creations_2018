# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0007_auto_20180902_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_entity',
            name='website',
            field=models.CharField(null=True, blank=True, max_length=70),
        ),
    ]
