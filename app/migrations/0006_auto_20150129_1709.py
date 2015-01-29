# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150129_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='image',
            field=models.ImageField(default=b'static/images/placehold_square.gif', upload_to=b'/Users/cts64/Documents/Projects/CS399/cs399-theatre/app/media//images/shows'),
            preserve_default=True,
        ),
    ]
