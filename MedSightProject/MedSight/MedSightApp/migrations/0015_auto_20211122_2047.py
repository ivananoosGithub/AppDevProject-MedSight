# Generated by Django 3.2.6 on 2021-11-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedSightApp', '0014_remove_patients_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]
