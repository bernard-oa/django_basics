# Generated by Django 4.2.1 on 2023-08-06 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0004_article_alter_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 6, 48, 13, 32389, tzinfo=datetime.timezone.utc)),
        ),
    ]