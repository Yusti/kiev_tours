# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=4096)),
                ('price', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('visible', models.BooleanField(default=False)),
                ('tourType', models.IntegerField(default=1, choices=[(0, 'Tour on weekend'), (1, 'Excursion tour'), (2, 'Personal guide')])),
            ],
        ),
        migrations.CreateModel(
            name='TourImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('visible', models.BooleanField(default=True)),
                ('mainImage', models.BooleanField(default=False)),
                ('tour', models.ForeignKey(to='tours.Tour')),
            ],
        ),
    ]
