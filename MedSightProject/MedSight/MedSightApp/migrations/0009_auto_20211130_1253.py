# Generated by Django 3.2.6 on 2021-11-30 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedSightApp', '0008_auto_20211130_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='apt_reason',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='apt_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='doctor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MedSightApp.doctors'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MedSightApp.patients'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
