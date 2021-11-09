from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *
# Create your views here.
class IndexView(View): 
    # Django inheritance definition 'MyIndexView(View)'
    # While in Java inheritance definition, this would be 'MyIndexView extends View'
    # 'View' is the Parent Class, 'MyIndexView' is the Child Class that you can name/rename
    def get(self, request): 
        # Single method to display index.html; 
        # 'def' meaning define; with 'get'
        # The method accepts 2 arguements:
        # 'self' meaning 'its own/self'
        # 'request' returns whatever the method performs
        # The 'return' of the method is to display/render to the browser 'index.html'
        return render(request, 'pages/index.html', {})

class HomeView(View): 
    def get(self, request): 
        return render(request, 'pages/Home.html', {})

class AboutView(View): 
    def get(self, request): 
        return render(request, 'pages/About.html', {})
        
class ContactView(View): 
    def get(self, request): 
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
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            if Users.objects.filter(username=username).count()>0:
                messages.info(request, 'Username already exists!')
                return redirect('MedSightApp:signup_view') 
            else:
                form = Users(username = username, password = password, firstname = firstname, lastname = lastname)
                form.save()
                check_user = Users.objects.filter(username=username, password=password, firstname = firstname, lastname = lastname)
                if check_user:
                    request.session['user'] = username
                    messages.info(request, 'Account successfully created! Please try to login.')
                    return redirect('MedSightApp:signin_view')
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
                return redirect('MedSightApp:signin_view')
            else:
                messages.info(request, 'Username and Password did not match! Please enter a valid Username and Password!')
                return redirect('MedSightApp:signin_view') 
        return render(request, 'pages/signin.html', {})

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('MedSightApp:signin_view')
    return redirect('MedSightApp:signin_view')