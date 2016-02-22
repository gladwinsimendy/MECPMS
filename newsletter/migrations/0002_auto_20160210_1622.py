# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 22, 22, 574715)),
        ),
    ]
