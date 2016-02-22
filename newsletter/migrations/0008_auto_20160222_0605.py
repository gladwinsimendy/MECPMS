# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20160222_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 22, 6, 5, 55, 615944), blank=True),
        ),
    ]
