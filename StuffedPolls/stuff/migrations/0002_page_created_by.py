# Generated by Django 2.0.4 on 2018-04-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_by',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
