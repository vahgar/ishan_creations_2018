# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0006_auto_20180221_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_entity',
            name='social_media',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
    ]
