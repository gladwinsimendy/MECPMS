# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0016_auto_20160312_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='batch',
            field=models.CharField(blank=True, max_length=200, editable=False, choices=[(b'CSA', b'CSA'), (b'CSB', b'CSB'), (b'ECA', b'ECA'), (b'ECB', b'ECB'), (b'EEE', b'EEE'), (b'BME', b'BME')]),
        ),
    ]
