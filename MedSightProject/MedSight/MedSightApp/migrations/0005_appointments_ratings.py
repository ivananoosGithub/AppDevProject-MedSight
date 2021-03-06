# Generated by Django 3.2.6 on 2021-11-24 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedSightApp', '0004_alter_users_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedSightApp.doctors')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedSightApp.patients')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('apt_type', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=20)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedSightApp.doctors')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedSightApp.patients')),
            ],
        ),
    ]
