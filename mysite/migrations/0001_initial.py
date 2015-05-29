# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('checked', models.BooleanField(default=False)),
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
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('tag', models.CharField(max_length=500)),
                ('main_image', models.CharField(max_length=200)),
                ('main_image_caption', models.CharField(max_length=400)),
                ('folder', models.CharField(unique=True, max_length=200)),
                ('style', models.CharField(max_length=200, choices=[(b'course', b'Course Work'), (b'extra', b'Extra Work'), (b'ongoing', b'R')])),
                ('alt_text', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
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
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=500)),
                ('conection', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
