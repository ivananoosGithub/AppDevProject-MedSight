from django import forms
from .models import *

# Create 'forms.py' when we begin/start to execute Django Queries and manipulate the database and its objects
# All forms are python classes that inherits from 'forms.ModelForm'
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields= '__all__'   # Refer to ALL the fields with the '__all__' keyword
        #fields = 'donor_id, first_name,last_name, contact_number, blood_type' # Select specific fields

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields= '__all__' 

class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        exclude = ['prefix']

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields= '__all__' 

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields= ['rating']