from django.db import models

# Create your models here.
# The tables will be created here, not in the phpMyAdmin database
# 'makemigrations' command to save the contents here then 'migrate'
# model inherits models.Model

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 20, unique=True)
    password = models.CharField(max_length = 20)
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
    contact_number = models.CharField(max_length = 20)
    current_address = models.CharField(max_length = 500)
    # <!-- TO BE FIXED profile_pic-->
    # profile_pic = models.ImageField(upload_to ='upload/', null=True)
    
    class meta:
        db_table = 'Patients' 

class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,to_field='username',on_delete = models.CASCADE) #foreign key syntax
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    contact_number = models.CharField(max_length = 20)
    current_address = models.CharField(max_length = 500)
    profile_pic = models.ImageField(upload_to='images', null=True)
    # <!-- TO BE FIXED med_license&profile_pic-->
    # med_license = models.ImageField(upload_to ='upload/', null=True)
    

    class meta:
        db_table = 'Doctors' 