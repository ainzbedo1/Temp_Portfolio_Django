# Generated by Django 2.1.7 on 2019-03-19 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='body',
            field=models.TextField(default='blah blah blah'),
        ),
        migrations.AlterField(
            model_name='main',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 19, 17, 4, 25, 317239)),
        ),
        migrations.AlterField(
            model_name='main',
            name='title',
            field=models.CharField(default='TEST TITLE 1', max_length=200),
        ),
    ]
