# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_auto_20160222_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
