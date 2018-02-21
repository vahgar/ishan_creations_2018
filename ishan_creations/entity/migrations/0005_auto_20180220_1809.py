# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0004_business_entity_image_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_entity',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='entity_pics/'),
        ),
        migrations.AddField(
            model_name='business_entity',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='entity_pics/'),
        ),
        migrations.AddField(
            model_name='business_entity',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='entity_pics/'),
        ),
    ]
