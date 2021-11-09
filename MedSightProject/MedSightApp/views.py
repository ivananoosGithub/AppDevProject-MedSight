from django.shortcuts import render

# Create your views here.


def home(response):
    return render(response, "MedSightApp/Home.html", {})


def contact(response):
    return render(response, "MedSightApp/Contact.html", {})


def about(response):
    return render(response, "MedSightApp/About.html", {})


def signin(response):
    return render(response, "MedSightApp/SignIn.html", {})


def signup(response):
    return render(response, "MedSightApp/SignUp.html", {})
