# Generated by Django 3.0.6 on 2020-06-04 07:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0003_breakingnews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breakingnews',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='sportnews',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 4, 7, 24, 7, 223714, tzinfo=utc)),
        ),
    ]
