# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='account',
            field=models.TextField(default=-1),
            preserve_default=False,
        ),
    ]
