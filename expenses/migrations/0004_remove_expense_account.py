# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expense_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='account',
        ),
    ]
