# Generated by Django 4.0.4 on 2022-12-14 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diva',
            name='isDiva',
        ),
        migrations.RemoveField(
            model_name='hunk',
            name='isDiva',
        ),
    ]
