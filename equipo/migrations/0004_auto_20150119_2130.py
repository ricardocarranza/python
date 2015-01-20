# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0003_equipo_tipo_de_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='tipo_de_equipo',
            field=models.ForeignKey(to='equipo.TipoEquipo'),
            preserve_default=True,
        ),
    ]
