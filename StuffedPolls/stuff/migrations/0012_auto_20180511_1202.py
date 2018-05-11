# Generated by Django 2.0.4 on 2018-05-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0011_faction_race'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='page_text',
        ),
        migrations.RemoveField(
            model_name='faction',
            name='title',
        ),
        migrations.RemoveField(
            model_name='race',
            name='page_text',
        ),
        migrations.RemoveField(
            model_name='race',
            name='title',
        ),
        migrations.AddField(
            model_name='faction',
            name='faction_info',
            field=models.CharField(default='Missing', max_length=1000),
        ),
        migrations.AddField(
            model_name='faction',
            name='faction_name',
            field=models.CharField(default='Missing', max_length=100),
        ),
        migrations.AddField(
            model_name='race',
            name='faction',
            field=models.CharField(choices=[('Alliance', 'Alliance'), ('Horde', 'Horde'), ('Allied', 'Allied Race')], default='none', max_length=8),
        ),
        migrations.AddField(
            model_name='race',
            name='race_info',
            field=models.CharField(default='Missing', max_length=1000),
        ),
        migrations.AddField(
            model_name='race',
            name='race_name',
            field=models.CharField(default='Missing', max_length=100),
        ),
    ]
