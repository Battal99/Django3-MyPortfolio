# Generated by Django 4.0.3 on 2022-04-09 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_blog',
            field=models.DateField(default=datetime.datetime(2022, 4, 9, 11, 54, 53, 989630)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
