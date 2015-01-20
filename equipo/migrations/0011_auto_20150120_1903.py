# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0010_auto_20150120_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fecha',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
