# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-19 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopit', '0003_rebuild_flag_mptt_tree'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandtranslation',
            name='description',
            field=models.TextField(blank=True, help_text="Description of a categorization, usually used as lead text in categorization's detail view.", verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='description',
            field=models.TextField(blank=True, help_text="Description of a categorization, usually used as lead text in categorization's detail view.", verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='manufacturertranslation',
            name='description',
            field=models.TextField(blank=True, help_text="Description of a categorization, usually used as lead text in categorization's detail view.", verbose_name='Description'),
        ),
    ]
