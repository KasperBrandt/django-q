# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_q', '0009_add_broker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='started',
            field=models.DateTimeField(editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='stopped',
            field=models.DateTimeField(editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='success',
            field=models.BooleanField(default=True, editable=False, db_index=True),
        ),
    ]
