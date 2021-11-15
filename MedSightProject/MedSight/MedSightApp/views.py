from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *
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
        else:
            return render(request, 'pages/index.html', {})

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
                pcnum = request.POST.get("contact_number")
                pcadd = request.POST.get("current_address")
                update_Patient = Patients.objects.filter(patient_id=pid).update(first_name = pfname, last_name = plname, contact_number = pcnum, current_address = pcadd)
                print(update_Patient)
                print('Patient record updated!')
            elif 'btnDeletePatient' in request.POST:
                print('Delete button clicked!')
                pid = request.POST.get("patient_id")
                Patients.objects.filter(patient_id=pid).delete()
                print("Patient record deleted")

            # Doctors Table
            if 'btnUpdateDoctor' in request.POST:
                print('Update button clicked!')
                did = request.POST.get("doctor_id")
                dfname = request.POST.get("first_name")
                dlname = request.POST.get("last_name")
                dcnum = request.POST.get("contact_number")
                dcadd = request.POST.get("current_address")
                update_Doctor = Doctors.objects.filter(doctor_id=did).update(first_name = dfname, last_name = dlname, contact_number = dcnum, current_address = dcadd)
                print(update_Doctor)
                print('Doctor record updated!')
            elif 'btnDeleteDoctor' in request.POST:
                print('Delete button clicked!')
                did = request.POST.get("doctor_id")
                Doctors.objects.filter(doctor_id=did).delete()
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
            email = request.POST.get("email")
            if Users.objects.filter(username=username).count()>0:
                messages.info(request, 'Username already exists!')
                return redirect('MedSightApp:signup_view') 
            else:
                form = Users(username = username, password = password, email = email)
                form.save()
                check_user = Users.objects.filter(username=username, password=password, email = email)
                if check_user:
                    request.session['user'] = username
                    return redirect('MedSightApp:role_view')
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
            check_user = Users.objects.filter(username=username, password=password)
            if check_user:
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
        return render(request, 'pages/signin.html', {})

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
            current_user = request.session['user']
            context = {
                'current_user': current_user
            }
        return render(request, 'pages/createPatient.html',context)
    def post(self, request):        
        form = PatientsForm(request.POST, request.FILES)   
        if form.is_valid():
            fk = form.cleaned_data.get("username")
            pfname = request.POST.get("first_name")
            plname = request.POST.get("last_name")
            pcnum = request.POST.get("contact_number")
            pcadd = request.POST.get("current_address")
            form = Patients(username = fk, first_name = pfname, last_name = plname, contact_number = pcnum, current_address = pcadd)
            form.save() 
            return redirect('MedSightApp:signin_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class CreateDoctorView(View):
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user
            }
        return render(request, 'pages/createDoctor.html',context)
    def post(self, request):        
        form = DoctorsForm(request.POST, request.FILES)        
        if form.is_valid():
            fk = form.cleaned_data.get("username")
            dfname = request.POST.get("first_name")
            dlname = request.POST.get("last_name")
            dcnum = request.POST.get("contact_number")
            dcadd = request.POST.get("current_address")
            form = Doctors(username = fk, first_name = dfname, last_name = dlname, contact_number = dcnum, current_address = dcadd)
            form.save() 
            return redirect('MedSightApp:signin_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('MedSightApp:signin_view')
    return redirect('MedSightApp:index_view')

class ProfileView(View): 
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
        return render(request, 'pages/Profile.html', context)

    def post(self, request):
       if request.method == 'POST':
           # Patients Table
            if 'btnUpdatePatient' in request.POST:
                print('Update button clicked!')
                pid = request.POST.get("patient_id")
                pfname = request.POST.get("first_name")
                plname = request.POST.get("last_name")
                pcnum = request.POST.get("contact_number")
                pcadd = request.POST.get("current_address")
                update_Patient = Patients.objects.filter(patient_id=pid).update(first_name = pfname, last_name = plname, contact_number = pcnum, current_address = pcadd)
                print(update_Patient)
                print('Patient account updated!')
                return redirect('MedSightApp:profile_view')
            elif 'btnDeletePatient' in request.POST:
                print('Delete button clicked!')
                pid = request.POST.get("patient_id")
                Patients.objects.filter(patient_id=pid).delete()
                print("Patient account deleted")
                return redirect('MedSightApp:index_view')
            
            # Doctors Table
            if 'btnUpdateDoctor' in request.POST:
                print('Update button clicked!')
                did = request.POST.get("doctor_id")
                dfname = request.POST.get("first_name")
                dlname = request.POST.get("last_name")
                dcnum = request.POST.get("contact_number")
                dcadd = request.POST.get("current_address")
                update_Doctor = Doctors.objects.filter(doctor_id=did).update(first_name = dfname, last_name = dlname, contact_number = dcnum, current_address = dcadd)
                print(update_Doctor)
                print('Doctor account updated!')
                return redirect('MedSightApp:profile_view')
            elif 'btnDeleteDoctor' in request.POST:
                print('Delete button clicked!')
                did = request.POST.get("doctor_id")
                Doctors.objects.filter(doctor_id=did).delete()
                print("Doctor account deleted")
                return redirect('MedSightApp:index_view')
                