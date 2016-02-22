# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_notifications_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
