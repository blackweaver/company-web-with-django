# Generated by Django 2.0.2 on 2018-08-10 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Services',
        ),
    ]