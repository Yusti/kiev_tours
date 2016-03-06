# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('visible', models.BooleanField(default=True)),
                ('mainImage', models.BooleanField(default=False)),
                ('tour', models.ForeignKey(to='tours.Tour')),
            ],
        ),
        migrations.RemoveField(
            model_name='tourimages',
            name='tour',
        ),
        migrations.DeleteModel(
            name='TourImages',
        ),
    ]
