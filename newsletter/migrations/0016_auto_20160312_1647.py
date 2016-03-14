# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0015_auto_20160310_1957'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_details',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='student_details',
            name='batch',
        ),
    ]
