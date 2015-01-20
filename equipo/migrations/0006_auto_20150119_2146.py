# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0005_auto_20150119_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='ram_capacidad',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 45, 22, 786466, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='ram_marca',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 46, 11, 234250, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='ram_slot',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 46, 20, 242665, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
