# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_auto_20150119_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='modelo',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 33, 34, 388551, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='moderboard_marca',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 33, 51, 860041, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='moderboard_modelo',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 34, 4, 707731, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='moderboard_tipo',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 34, 20, 20025, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='serie_caja',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 34, 30, 483891, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
    ]
