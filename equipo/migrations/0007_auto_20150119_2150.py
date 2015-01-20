# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0006_auto_20150119_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fuente_marca',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 50, 15, 25675, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='fuente_pines',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 50, 23, 633072, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='fuente_potencia',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 50, 36, 17598, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ram_marca',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
