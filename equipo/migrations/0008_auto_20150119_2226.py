# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0007_auto_20150119_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad_optica', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='equipo',
            name='disco_duro_capacidad',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 22, 25, 40, 509060, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='disco_duro_interfaz',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 22, 25, 49, 469313, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='disco_duro_marca',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 22, 25, 58, 236692, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='procesador_interfaz',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 22, 26, 8, 172861, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='procesador_marca',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 22, 26, 16, 365364, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='procesador_referencia',
            field=models.CharField(default=datetime.datetime(2015, 1, 19, 22, 26, 25, 149281, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='unidades_opticas',
            field=models.ManyToManyField(to='equipo.Unidad'),
            preserve_default=True,
        ),
    ]
