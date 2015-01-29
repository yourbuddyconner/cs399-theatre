# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150129_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.ImageField(default=b'images/placehold_square.gif', upload_to=b'images/shows'),
            preserve_default=True,
        ),
    ]
