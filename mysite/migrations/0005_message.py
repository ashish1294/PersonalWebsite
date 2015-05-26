# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20150320_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('checked', models.BooleanField()),
            ],
        ),
    ]
