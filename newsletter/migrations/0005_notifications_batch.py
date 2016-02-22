# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_sellerprofile_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='batch',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'CSA', b'CSA'), (b'CSB', b'CSB'), (b'ECA', b'ECA'), (b'ECB', b'ECB'), (b'EEE', b'EEE'), (b'BME', b'BME')]),
        ),
    ]
