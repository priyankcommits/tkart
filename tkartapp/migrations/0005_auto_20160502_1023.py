# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkartapp', '0004_auto_20160502_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shirt',
            old_name='shirt_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='shirt',
            old_name='shirt_name',
            new_name='name',
        ),
    ]