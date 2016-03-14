# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0023_auto_20160314_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='batch',
        ),
    ]
