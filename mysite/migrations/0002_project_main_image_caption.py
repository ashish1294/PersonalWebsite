# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_image_caption',
            field=models.CharField(default='Default For Now', max_length=400),
            preserve_default=False,
        ),
    ]
