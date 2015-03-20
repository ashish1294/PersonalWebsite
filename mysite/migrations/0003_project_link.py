# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_project_main_image_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='https://github.com/Bug-Assassins/DFC_query_builder', max_length=500),
            preserve_default=False,
        ),
    ]
