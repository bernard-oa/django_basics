# Generated by Django 4.2.1 on 2023-08-02 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 2, 11, 55, 46, 60641, tzinfo=datetime.timezone.utc)),
        ),
    ]