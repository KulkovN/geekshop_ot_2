# Generated by Django 3.2.3 on 2021-07-24 20:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 26, 20, 29, 1, 331461, tzinfo=utc)),
        ),
    ]
