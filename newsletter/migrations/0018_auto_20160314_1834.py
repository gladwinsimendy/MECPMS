# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0017_student_details_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='batch',
            field=models.CharField(blank=True, max_length=200, choices=[(b'CSA', b'CSA'), (b'CSB', b'CSB'), (b'ECA', b'ECA'), (b'ECB', b'ECB'), (b'EEE', b'EEE'), (b'BME', b'BME')]),
        ),
    ]
