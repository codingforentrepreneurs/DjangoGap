# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_auto_20141111_0540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posting',
            options={'ordering': ['-updated', '-timestamp']},
        ),
        migrations.RemoveField(
            model_name='posting',
            name='post',
        ),
        migrations.AddField(
            model_name='posting',
            name='title',
            field=models.CharField(default=b'Title', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posting',
            name='url',
            field=models.URLField(default=b'http://youtube.com/', max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posting',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 13, 22, 57, 38, 90833, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posting',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 13, 22, 57, 38, 90874, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
