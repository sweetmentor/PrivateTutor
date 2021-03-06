# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0002_tutor_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='description',
            field=models.TextField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(default='images/default-image.jpg', upload_to='avatars'),
        ),
    ]
