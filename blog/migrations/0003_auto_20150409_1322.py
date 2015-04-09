# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140704_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
