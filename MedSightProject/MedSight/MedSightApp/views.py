from django.contrib import messages
from django.shortcuts import render, redirect
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
            context = {
                'current_user': current_user,
            }
        return render(request, 'pages/index.html', {})

class AdminView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
            return render(request, 'pages/Admin.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 

class PatientHomeView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
            return render(request, 'pages/LandingP.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 

class DoctorHomeView(View): 
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
            return render(request, 'pages/LandingD.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 

class AboutView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
        return render(request, 'pages/About.html', context)
        
class ContactView(View): 
    def get(self, request): 
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
        return render(request, 'pages/Contact.html', context)

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
    return redirect('MedSightApp:signin_view')

