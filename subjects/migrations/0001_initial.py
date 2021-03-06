# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects_tutor', to='tutors.Tutor')),
            ],
        ),
    ]
