# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_auto_20160308_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='marks_obtained',
            field=models.IntegerField(null=True),
        ),
    ]
