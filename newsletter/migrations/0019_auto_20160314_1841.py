# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0018_auto_20160314_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='batch',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
