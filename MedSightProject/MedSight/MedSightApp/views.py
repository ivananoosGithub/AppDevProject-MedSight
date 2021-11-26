from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *
from passlib.hash import pbkdf2_sha256
import os
# Create your views here.
class IndexView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']
            patients = Patients.objects.filter(username=current_user)     
            doctors = Doctors.objects.filter(username=current_user)

            context = {
                'current_user': current_user,
                'patients' : patients,
                'doctors' : doctors,
            }
            return render(request, 'pages/index.html', context)
            # return render(request, 'pages/UserLandingPage.html', context)
        else:
            return render(request, 'pages/index.html', {})
            # return render(request, 'pages/UserLandingPage.html.html', {})

class AdminView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            patients = Patients.objects.all()
            doctors = Doctors.objects.all()
            context = {
                'current_user': current_user,
                'patients' : patients,
                'doctors' : doctors,
            }
            return render(request, 'pages/Admin.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 
    def post(self, request):
       if request.method == 'POST':
           # Patients Table
            if 'btnUpdatePatient' in request.POST:
                print('Update button clicked!')
                pid = request.POST.get("patient_id")
                pfname = request.POST.get("first_name")
                plname = request.POST.get("last_name")
                pgend = request.POST.get("gender")  
                pcnum = request.POST.get("contact_number")
                pcadd = request.POST.get("current_address")
                update_Patient = Patients.objects.filter(patient_id=pid).update(first_name = pfname, last_name = plname, gender = pgend, contact_number = pcnum, current_address = pcadd)
                print(update_Patient)
                print('Patient record updated!')
            elif 'btnDeletePatient' in request.POST:
                print('Delete button clicked!')
                pid = request.POST.get("patient_id")
                Patients.objects.filter(patient_id=pid).delete()
                Users.objects.filter(user_id=pid).delete()
                print("Patient record deleted")

            # Doctors Table
            if 'btnUpdateDoctor' in request.POST:
                print('Update button clicked!')
                did = request.POST.get("doctor_id")
                dfname = request.POST.get("first_name")
                dlname = request.POST.get("last_name")
                dgend = request.POST.get("gender")  
                dcnum = request.POST.get("contact_number")
                dcadd = request.POST.get("current_address")
                update_Doctor = Doctors.objects.filter(doctor_id=did).update(first_name = dfname, last_name = dlname, gender = dgend, contact_number = dcnum, current_address = dcadd)
                print(update_Doctor)
                print('Doctor record updated!')
            elif 'btnDeleteDoctor' in request.POST:
                print('Delete button clicked!')
                did = request.POST.get("doctor_id")
                Doctors.objects.filter(doctor_id=did).delete()
                Users.objects.filter(user_id=did).delete()
                print("Doctor record deleted")

            return redirect('MedSightApp:admin_view')
class PatientHomeView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            patients = Patients.objects.filter(username=current_user)     

            context = {
                'current_user': current_user,
                'patients' : patients,
            }
            return render(request, 'pages/LandingP.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 

class DoctorHomeView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            doctors = Doctors.objects.filter(username=current_user)

            context = {
                'current_user': current_user,
                'doctors' : doctors,
            }
            return render(request, 'pages/LandingD.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 

class AboutView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']
            patients = Patients.objects.filter(username=current_user)     
            doctors = Doctors.objects.filter(username=current_user)

            context = {
                'current_user': current_user,
                'patients' : patients,
                'doctors' : doctors,
            }
            return render(request, 'pages/About.html', context)
        else:
            return render(request, 'pages/About.html', {})
        
        
class ContactView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']
            patients = Patients.objects.filter(username=current_user)     
            doctors = Doctors.objects.filter(username=current_user)

            context = {
                'current_user': current_user,
                'patients' : patients,
                'doctors' : doctors,
            }
            return render(request, 'pages/Contact.html', context)
        else:
            return render(request, 'pages/Contact.html', {})

class SignUpView(View): 
    def get(self, request):
        return render(request, 'pages/SignUp.html', {})
    def post(self, request):        
        form = UsersForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            confirmpassword = request.POST.get("confirmpassword")
            enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
            email = request.POST.get("email")
            if(confirmpassword == password):
                if Users.objects.filter(username=username).count()>0:
                    messages.info(request, 'Username already exists!')
                    return redirect('MedSightApp:signup_view') 
                else:
                    form = Users(username = username, password = enc_password, email = email)
                    form.save()
                    check_user = Users.objects.filter(username=username, password=enc_password, email = email)
                    if check_user:
                        request.session['user'] = username
                        return redirect('MedSightApp:role_view')
            else:
                messages.info(request, 'Passwords do not match!')
                return redirect('MedSightApp:signup_view')
        else:
            print(form.errors)
            messages.info(request, 'Account already exists! Please try another unique one.')
            return redirect('MedSightApp:signup_view') 

class SignInView(View): 
    def get(self, request):
        return render(request, 'pages/SignIn.html', {})
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            check_password = pbkdf2_sha256.hash(password, rounds=20000, salt_size=16)
            dec_password = pbkdf2_sha256.verify(password, check_password)
            check_user = Users.objects.filter(username=username)
            if check_user and dec_password:
                request.session['user'] = username
                if Patients.objects.filter(username=username).count()>0:
                    return redirect('MedSightApp:patientHome_view')
                elif Doctors.objects.filter(username=username).count()>0:
                    return redirect('MedSightApp:doctorHome_view')
                elif Users.objects.filter(username="admin").count()>0:
                    return redirect('MedSightApp:admin_view')
            else:
                messages.info(request, 'Incorrect Username and Password!')
                return redirect('MedSightApp:signin_view') 
        return redirect('MedSightApp:index_view')

class RoleView(View):
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
            return render(request, 'pages/role.html', context)
        else:
            return HttpResponse('Please do the initial registration to view this page.')

class CreatePatientView(View):
    def get(self, request):
        if 'user' in request.session:
            if Patients.objects.filter(username=request.session['user']) or Doctors.objects.filter(username=request.session['user']):
                return HttpResponse('You have already registered as a Patient or Doctor.')  
            else:
                current_user = request.session['user']
                context = {
                    'current_user': current_user
                }
                return render(request, 'pages/createPatient.html',context)
        else:
            return HttpResponse('Please do the initial registration to view this page.')
    def post(self, request):        
        form = PatientsForm(request.POST, request.FILES)   
        if form.is_valid():
            fk = form.cleaned_data.get("username")
            pfname = request.POST.get("first_name")
            plname = request.POST.get("last_name")
            pgend = request.POST.get("gender")    
            pcnum = request.POST.get("contact_number")
            pcadd = request.POST.get("current_address")
            ppp = request.FILES["profile_pic"]
            form = Patients(username = fk, first_name = pfname, last_name = plname, gender = pgend, contact_number = pcnum, current_address = pcadd, profile_pic = ppp)
            form.save() 
            return redirect('MedSightApp:patientHome_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class CreateDoctorView(View):
    def get(self, request):
        if 'user' in request.session:
            if Patients.objects.filter(username=request.session['user']) or Doctors.objects.filter(username=request.session['user']):
                return HttpResponse('You have already registered as a Patient or Doctor.')  
            else:
                current_user = request.session['user']
                context = {
                    'current_user': current_user
                }
                return render(request, 'pages/createDoctor.html',context)
        else:
            return HttpResponse('Please do the initial registration to view this page.')
    def post(self, request):        
        form = DoctorsForm(request.POST, request.FILES)        
        if form.is_valid() and form.is_multipart():
            fk = form.cleaned_data.get("username")
            dfname = request.POST.get("first_name")
            dlname = request.POST.get("last_name")
            dgend = request.POST.get("gender")            
            dcnum = request.POST.get("contact_number")
            dcadd = request.POST.get("current_address")
            dspc = request.POST.get("specialization")
            dexp = request.POST.get("experience")
            dprefm = "Dr."
            dpreff = "Dra."
            dpp = request.FILES["profile_pic"]

            if 'Male' in request.POST.get("gender"):                          
                form = Doctors(username = fk, prefix = dprefm, first_name = dfname, last_name = dlname, gender = dgend, contact_number = dcnum, current_address = dcadd, specialization = dspc, experience = dexp, profile_pic = dpp)
            else:
                form = Doctors(username = fk, prefix = dpreff, first_name = dfname, last_name = dlname, gender = dgend, contact_number = dcnum, current_address = dcadd, specialization = dspc, experience = dexp, profile_pic = dpp)
            form.save() 
            return redirect('MedSightApp:doctorHome_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('MedSightApp:signin_view')
    return redirect('MedSightApp:index_view')

class DProfileView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']  
            doctors = Doctors.objects.filter(username=current_user)
            user = Users.objects.filter(username=current_user)
            context = {
                'current_user': current_user,
                'doctors' : doctors,
                'user' : user,
            }
            return render(request, 'pages/Doctor-Profile.html', context)

    def post(self, request):
        if request.method == 'POST':
            # Doctors Table
            if 'btnUpdateDoctorD1' in request.POST:
                print('Update button clicked!')
                did = request.POST.get("doctor_id")
                dfname = request.POST.get("first_name")
                dlname = request.POST.get("last_name")
                dgend = request.POST.get("gender") 
                dcnum = request.POST.get("contact_number")
                dcadd = request.POST.get("current_address")                
                update_Doctor = Doctors.objects.filter(doctor_id=did).update(first_name = dfname, last_name = dlname, gender = dgend, contact_number = dcnum, current_address = dcadd)
                print(update_Doctor)
                print('Doctor account updated!')
                return redirect('MedSightApp:dprofile_view')

            elif 'btnUpdateDoctorD2' in request.POST:
                print('Update button clicked!')
                did = request.POST.get("doctor_id")
                dspc = request.POST.get("specialization")
                dexp = request.POST.get("experience")
                update_Doctor = Doctors.objects.filter(doctor_id=did).update(specialization = dspc, experience = dexp)
                print(update_Doctor)
                print('Doctor account updated!')
                return redirect('MedSightApp:dprofile_view')

            elif 'btnDeleteDoctorD' in request.POST:
                print('Delete button clicked!')
                did = request.POST.get("doctor_id")
                Doctors.objects.filter(doctor_id=did).delete()
                if 'user' in request.session:
                    current_user = request.session['user']
                Users.objects.filter(username=current_user).delete()
                print("Doctor account deleted")
                return redirect('MedSightApp:logout')

            # Update uploaded picture doesn't work yet
            elif 'btnPicDoctor' in request.POST:
                print('Update button clicked!')
                did = request.POST.get("doctor_id")
                m = Doctors.objects.get(doctor_id=did)
                m.dpp = request.FILES['profile_pic']
                update_Doctor = Doctors.objects.filter(doctor_id=did).update(profile_pic=m.dpp)
                print(update_Doctor)
                print('Doctor account updated!')
                return redirect("MedSightApp:dprofile_view")

class PProfileView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']  
            patients = Patients.objects.filter(username=current_user)
            user = Users.objects.filter(username=current_user)
            context = {
                'current_user': current_user,
                'patients' : patients,
                'user' : user,
            }
            return render(request, 'pages/Patient-Profile.html', context)

    def post(self, request):
       if request.method == 'POST':
           # Patients Table
            if 'btnUpdatePatientP' in request.POST:
                print('Update button clicked!')
                pid = request.POST.get("patient_id")
                pfname = request.POST.get("first_name")
                plname = request.POST.get("last_name")
                pgend = request.POST.get("gender") 
                pcnum = request.POST.get("contact_number")
                pcadd = request.POST.get("current_address")
                # ppp = request.FILES["profile_pic"]
                update_Patient = Patients.objects.filter(patient_id=pid).update(first_name = pfname, last_name = plname, gender = pgend, contact_number = pcnum, current_address = pcadd)#, profile_pic = ppp)
                print(update_Patient)
                print('Patient account updated!')
                return redirect('MedSightApp:pprofile_view')

            elif 'btnDeletePatientP' in request.POST:
                print('Delete button clicked!')
                pid = request.POST.get("patient_id")
                Patients.objects.filter(patient_id=pid).delete()
                if 'user' in request.session:
                    current_user = request.session['user']
                Users.objects.filter(username=current_user).delete()
                print("Patient record deleted")
                return redirect('MedSightApp:logout')

            # Update uploaded picture doesn't work yet
            elif 'btnPicPatient' in request.POST:
                print('Update button clicked!')
                pid = request.POST.get("patient_id")
                m = Doctors.objects.get(patient_id=pid)
                m.ppp = request.FILES['profile_pic']
                update_Patient = Doctors.objects.filter(patient_id=pid).update(profile_pic=m.ppp)
                print(update_Patient)
                print('Patient account updated!')
                return redirect("MedSightApp:pprofile_view")
         
# temporary view for backend purposes
class FindDoctorView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            patients = Patients.objects.all()
            doctors = Doctors.objects.all()
            context = {
                'current_user': current_user,
                'patients' : patients,
                'doctors' : doctors,
            }
            return render(request, 'pages/FindDocPage.html', context)
        else:
            return HttpResponse('Please login first to view this page.')

    def post(self, request):
        if request.method == 'POST':
            current_doctor = request.POST.get("doctor_id")
            request.session['doctor'] = current_doctor
            return redirect("MedSightApp:appointmentP_view")
        return render(request, 'pages/FindDocPage.html', {})

class AppointmentPageView(View):
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            current_doctor = request.session['doctor']
            patients = Patients.objects.all()
            doctors = Doctors.objects.all()
            users = Users.objects.all()
            context = {
                'current_user': current_user,
                'current_doctor': current_doctor,
                'patients' : patients,
                'doctors' : doctors,
                'users' : users,
            }
            return render(request, 'pages/AppointmentPage.html', context)
        else:
            return HttpResponse('Please login first to view this page.')

    def post(self, request):        
        form = AppointmentsForm(request.POST, request.FILES)   
        if form.is_valid():
            fk = form.cleaned_data.get("username")
            pfname = request.POST.get("first_name")
            plname = request.POST.get("last_name")
            pgend = request.POST.get("gender")    
            pcnum = request.POST.get("contact_number")
            pcadd = request.POST.get("current_address")
            ppp = request.FILES["profile_pic"]
            form = Patients(username = fk, first_name = pfname, last_name = plname, gender = pgend, contact_number = pcnum, current_address = pcadd, profile_pic = ppp)
            form.save() 
            return redirect('MedSightApp:patientHome_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')