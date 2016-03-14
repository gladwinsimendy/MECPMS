# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_auto_20160222_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='marks_obtained',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='approved',
            field=models.CharField(max_length=10, choices=[(b'YES', b'YES'), (b'NO', b'NO')]),
        ),
    ]
