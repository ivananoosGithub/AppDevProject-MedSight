from django.db import models

# Create your models here.
# The tables will be created here, not in the phpMyAdmin database
# 'makemigrations' command to save the contents here then 'migrate'
# model inherits models.Model

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 20, unique=True)
    password = models.CharField(max_length = 20)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)

    class meta:
        db_table = 'Users'

    def __str__(self):
        return self.username