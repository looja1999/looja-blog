# Generated by Django 3.0.8 on 2020-07-29 03:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20200729_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 3, 3, 23, 493357, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 3, 3, 23, 492360, tzinfo=utc)),
        ),
    ]
