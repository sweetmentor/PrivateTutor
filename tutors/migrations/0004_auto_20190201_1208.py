# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0003_auto_20190201_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(default='no_image.jpg', upload_to='avatars'),
        ),
    ]
