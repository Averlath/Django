# Generated by Django 2.0.5 on 2018-05-14 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alliancecharacter',
            name='article_created_by',
        ),
        migrations.RemoveField(
            model_name='hordecharacter',
            name='article_created_by',
        ),
    ]