from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.urls import path
from MedSightApp import views # App from myapp1 directory folder. Import html files or classes from views.py

app_name = 'MedSightApp' # Specify the app name (myapp1)

urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('', views.IndexView.as_view(), name="index_view"), 
    # To replace "success page" and default the index page with '' (blank).
    #Specifies the path for index.html
    # Name the attribute of the path the same as the class but with underscores: "my_index_view"
    # MyIndexView is the name of the class from views.py
    # Create/Specify one path for everytime you want to render/view a html file in a browser
    path('about/', views.AboutView.as_view(), name="about_view"),
    path('contact/', views.ContactView.as_view(), name="contact_view"),
    path('signin/', views.SignInView.as_view(), name="signin_view"),
    path('signup/', views.SignUpView.as_view(), name="signup_view"),
    path('role/', views.RoleView.as_view(), name="role_view"),
    path('createPatient/', views.CreatePatientView.as_view(), name="createPatient_view"),
    path('createDoctor/', views.CreateDoctorView.as_view(), name="createDoctor_view"),
    path('landing_p/', views.PatientHomeView.as_view(), name="patientHome_view"),
    path('landing_d/', views.DoctorHomeView.as_view(), name="doctorHome_view"),
    path('admin/', views.AdminView.as_view(), name="admin_view"),
    path('logout/', views.logout, name='logout'),
    
    path('doctor-profile/', views.DProfileView.as_view(), name="dprofile_view"),
    path('patient-profile/', views.PProfileView.as_view(), name="pprofile_view"),

    # temporary url for backend purposes
    path('findDoctor/', views.FindDoctorView.as_view(), name="finddoc_view"),
    path('viewDoctor/', views.ViewDoctorView.as_view(), name="viewdoc_view"),
    path('appointmentPage/', views.AppointmentPageView.as_view(), name="appointmentP_view"),
    path('editAppointmentP/', views.EditAppointmentPView.as_view(), name="editappointmentP_view"),
    path('editAppointmentD/', views.EditAppointmentDView.as_view(), name="editappointmentD_view"),
    path('rateDoctor/', views.RateDoctorView.as_view(), name="ratedoc_view"),
    path('appointment/', views.FinalAppointmentView.as_view(), name="appointment_view"),
    path('rating/',views.RatingsView.as_view(), name="rating_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)