# Generated by Django 3.2.5 on 2021-08-27 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0007_alter_topic_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 27, 18, 7, 55, 800085, tzinfo=utc), verbose_name='Published Date'),
        ),
    ]
