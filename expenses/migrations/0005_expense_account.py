# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_account'),
        ('expenses', '0004_remove_expense_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='account',
            field=models.ForeignKey(default=None, to='users.Account'),
            preserve_default=False,
        ),
    ]
