# Generated by Django 3.2.6 on 2021-11-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedSightApp', '0007_auto_20211116_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='med_license',
            field=models.FileField(null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='upload/'),
        ),
    ]