# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, serialize=False,
                    verbose_name='ID', primary_key=True)),
                ('name', models.CharField(
                    max_length=200, verbose_name='Movie Name', unique=True)),
            ],
        ),
    ]
