# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20150119_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='tipo_de_equipo',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 21, 27, 24, 596363, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
    ]
