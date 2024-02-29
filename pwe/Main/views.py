from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Create a new Contact object and save it to the database
        new_contact = Contact.objects.create(name=name, email=email, address=address, message=message)

        # Redirect the user to a thank you page or any other appropriate page after successful submission
        return HttpResponse('Thank you for your message!')

    return render(request, 'contact.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect('post')
        else:
            messages.info(request, 'Wrong passwrod or username')
            return redirect('user_login')
    return render(request, 'login.html')



