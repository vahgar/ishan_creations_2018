# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0005_auto_20180220_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display_pics',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('images', models.ImageField(upload_to='entity_pics/', blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='business_entity',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='business_entity',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='business_entity',
            name='image_4',
        ),
        migrations.AddField(
            model_name='display_pics',
            name='entity',
            field=models.ForeignKey(to='entity.Business_Entity'),
        ),
    ]
