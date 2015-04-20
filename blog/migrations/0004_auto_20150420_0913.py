# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150409_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='embed_code',
            field=models.TextField(help_text=b'The embed code for the video', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='image_url',
            field=models.URLField(help_text=b'The image url', blank=True),
        ),
    ]
