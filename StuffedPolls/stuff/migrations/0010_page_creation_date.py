# Generated by Django 2.0.4 on 2018-04-27 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0009_auto_20180426_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation_date'),
            preserve_default=False,
        ),
    ]
