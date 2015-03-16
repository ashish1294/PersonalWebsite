# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('tag', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('main_image', models.CharField(max_length=200)),
                ('folder', models.CharField(unique=True, max_length=200)),
                ('style', models.CharField(max_length=200, choices=[(b'course', b'Course Work'), (b'extra', b'Extra Work'), (b'research', b'RESEARCH')])),
                ('alt_text', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='project_tab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('proj', models.ForeignKey(to='mysite.project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
