# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0013_auto_20160309_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='batch',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
