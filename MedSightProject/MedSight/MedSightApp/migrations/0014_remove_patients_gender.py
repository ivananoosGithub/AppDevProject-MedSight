# Generated by Django 3.2.6 on 2021-11-22 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MedSightApp', '0013_auto_20211122_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='gender',
        ),
    ]
