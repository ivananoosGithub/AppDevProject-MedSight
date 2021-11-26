from django.db import models
from passlib.hash import pbkdf2_sha256
# Create your models here.
# The tables will be created here, not in the phpMyAdmin database
# 'makemigrations' command to save the contents here then 'migrate'
# model inherits models.Model

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 20, unique=True)
    password = models.CharField(max_length = 256)
    email = models.CharField(max_length = 50)

    class meta:
        db_table = 'Users'

    def __str__(self):
        return self.username

class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,to_field='username',on_delete = models.CASCADE) #foreign key syntax
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 10)
    contact_number = models.CharField(max_length = 20)
    current_address = models.CharField(max_length = 500)
    profile_pic = models.ImageField(upload_to='images', null=True)
    
    class meta:
        db_table = 'Patients' 

class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,to_field='username',on_delete = models.CASCADE) #foreign key syntax
    prefix = models.CharField(max_length = 5)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 10)
    contact_number = models.CharField(max_length = 20)
    current_address = models.CharField(max_length = 500)
    specialization = models.CharField(max_length = 50)
    experience = models.CharField(max_length = 5)
    profile_pic = models.ImageField(upload_to='images', null=True)    

    class meta:
        db_table = 'Doctors' 

class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, to_field='patient_id', on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(Doctors, to_field='doctor_id', on_delete = models.CASCADE)
    apt_type = models.CharField(max_length = 10)
    apt_reason = models.CharField(max_length = 30)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20)

class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, to_field='patient_id', on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(Doctors, to_field='doctor_id', on_delete = models.CASCADE)
    rating = models.IntegerField() 