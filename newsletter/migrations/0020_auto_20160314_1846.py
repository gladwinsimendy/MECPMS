# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0019_auto_20160314_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='batch',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
    ]
