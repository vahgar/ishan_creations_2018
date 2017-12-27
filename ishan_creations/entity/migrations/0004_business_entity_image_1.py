# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_auto_20171220_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_entity',
            name='image_1',
            field=models.FileField(null=True, upload_to='entity_pics/', blank=True),
        ),
    ]
