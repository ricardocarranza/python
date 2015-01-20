# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0009_auto_20150120_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fecha',
            field=models.DateField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='pc',
            field=models.CharField(default=datetime.datetime(2015, 1, 20, 19, 2, 20, 570523, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='usuario',
            field=models.CharField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
    ]
