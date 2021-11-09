from django.urls import path

from . import views

# app_name = 'Website'

urlpatterns = [

    # HOME PAGE
    path('', views.home, name="Home"),
    path("Contact", views.contact, name="Contact"),
    path("About", views.about, name="About"),
    path("SignIn", views.signin, name="SignIn"),
    path("SignUp", views.signup, name="SignUp"),
]
