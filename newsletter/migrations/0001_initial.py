# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='adminregister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('Managing_class', models.CharField(blank=True, max_length=200, null=True, choices=[(b'CSA', b'CSA'), (b'CSB', b'CSB'), (b'ECA', b'ECA'), (b'ECB', b'ECB'), (b'EEE', b'EEE'), (b'BME', b'BME')])),
                ('project_type', models.CharField(blank=True, max_length=200, null=True, choices=[(b'MINI', b'MINIPROJECT'), (b'MAIN', b'MAINPROJECT')])),
                ('faculty', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gpno', models.IntegerField(null=True)),
                ('time_stamp', models.DateTimeField(default=b'2015-02-12 00:00')),
                ('doc_title', models.CharField(max_length=200)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('docdesc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idno', models.IntegerField(null=True)),
                ('notification', models.CharField(max_length=1000)),
                ('category', models.CharField(default=b'private', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sellerprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(max_length=200, null=True, blank=True)),
                ('batch', models.CharField(blank=True, max_length=200, null=True, choices=[(b'CSA', b'CSA'), (b'CSB', b'CSB'), (b'ECA', b'ECA'), (b'ECB', b'ECB'), (b'EEE', b'EEE'), (b'BME', b'BME')])),
                ('ptype', models.CharField(blank=True, max_length=200, null=True, choices=[(b'MINI', b'MINIPROJECT'), (b'MAIN', b'MAINPROJECT')])),
                ('seller', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=200, null=True, blank=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('rollno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ForeignKey(related_name='member', to='newsletter.sellerprofile')),
            ],
        ),
    ]
