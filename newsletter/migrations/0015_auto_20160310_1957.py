# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0014_student_details_batch'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_details',
            unique_together=set([('rollno', 'batch')]),
        ),
    ]
