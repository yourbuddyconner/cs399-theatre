# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_show_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='image',
            field=models.ImageField(default=b'static/images/placehold_square.gif', upload_to=b'static/images/shows'),
            preserve_default=True,
        ),
    ]
