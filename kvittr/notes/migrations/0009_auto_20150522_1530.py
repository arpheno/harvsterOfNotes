# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20150522_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
