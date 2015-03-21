# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_project_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_tab',
            name='proj',
        ),
        migrations.DeleteModel(
            name='project_tab',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AlterField(
            model_name='project',
            name='style',
            field=models.CharField(max_length=200, choices=[(b'course', b'Course Work'), (b'extra', b'Extra Work'), (b'ongoing', b'R')]),
            preserve_default=True,
        ),
    ]
