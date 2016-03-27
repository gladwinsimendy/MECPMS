# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0024_remove_student_details_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminregister',
            name='batch_year',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020'), (b'2021', b'2021')]),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='batch_year',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020'), (b'2021', b'2021')]),
        ),
    ]
