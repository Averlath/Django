# Generated by Django 2.0.4 on 2018-04-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0006_auto_20180425_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(null=True, upload_to='templates/images'),
        ),
    ]
