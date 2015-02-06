# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_merchandise'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_url',
            field=models.CharField(max_length=100, default='/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='image',
            field=models.ImageField(upload_to='images/shows', default='static/images/placehold_square.gif'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='end_date',
            field=models.DateField(verbose_name='day the show ends'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='image',
            field=models.ImageField(upload_to='images/shows', default='static/images/placehold_square.gif'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='start_date',
            field=models.DateField(verbose_name='day the show begins'),
            preserve_default=True,
        ),
    ]
