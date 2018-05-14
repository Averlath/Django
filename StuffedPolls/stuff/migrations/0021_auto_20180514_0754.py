# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-14 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0020_remove_character_race'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllianceCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(default=b'', max_length=100)),
                ('allied_with', models.CharField(choices=[(b'Choose', b'Choose...'), (b'Alliance', b'Alliance'), (b'Horde', b'Horde')], default=b'', max_length=8)),
                ('status', models.CharField(choices=[(b'Alive', b'Alive'), (b'Dead', b'Dead'), (b'Incapacitated', b'Incapacitated'), (b'Unknown', b'Unknown')], default=b'', max_length=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'images')),
                ('race', models.CharField(choices=[(b'Human', b'Human'), (b'Dwarf', b'Dwarf'), (b'Night Elf', b'Night Elf'), (b'Gnome', b'Gnome'), (b'Draenei', b'Draenei'), (b'Worgen', b'Worgen'), (b'Pandaren', b'Pandaren')], max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HordeCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(default=b'', max_length=100)),
                ('allied_with', models.CharField(choices=[(b'Choose', b'Choose...'), (b'Alliance', b'Alliance'), (b'Horde', b'Horde')], default=b'', max_length=8)),
                ('status', models.CharField(choices=[(b'Alive', b'Alive'), (b'Dead', b'Dead'), (b'Incapacitated', b'Incapacitated'), (b'Unknown', b'Unknown')], default=b'', max_length=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'images')),
                ('race', models.CharField(choices=[(b'Orc', b'Orc'), (b'Undead', b'Undead'), (b'Tauren', b'Tauren'), (b'Troll', b'Troll'), (b'Blood Elf', b'Blood Elf'), (b'Goblin', b'Goblin'), (b'Pandaren', b'Pandaren')], max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Character',
        ),
    ]
