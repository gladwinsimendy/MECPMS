# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20160210_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
