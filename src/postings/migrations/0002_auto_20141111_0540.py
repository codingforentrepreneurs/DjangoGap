# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 5, 40, 23, 142199, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posting',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 5, 40, 23, 142265, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
