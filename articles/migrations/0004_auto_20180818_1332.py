# Generated by Django 2.1 on 2018-08-18 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180818_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles_news',
            name='date',
        ),
        migrations.AlterField(
            model_name='articles_analyse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 12, 32, 17, 969996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='articles_tutorial',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 12, 32, 17, 969996, tzinfo=utc)),
        ),
    ]
