# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.TextField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog_visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('user_agent', models.TextField()),
                ('blog', models.ForeignKey(to='mysite.blog')),
            ],
        ),
        migrations.CreateModel(
            name='error_404_visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('user_agent', models.TextField()),
                ('url_requested', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='normal_visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('user_agent', models.TextField()),
                ('page', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='project_visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('user_agent', models.TextField()),
                ('project', models.ForeignKey(to='mysite.project')),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
