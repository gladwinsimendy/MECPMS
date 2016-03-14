# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0020_auto_20160314_1846'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_details',
            unique_together=set([('rollno', 'batch')]),
        ),
    ]
