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



from django.shortcuts import render
from .models import Leave

def leave_request(request):
    message = None
    if request.method == 'POST':
        # Get form data from POST request
        user = request.user
        contact_number = request.POST.get('contact_number')
        reason = request.POST.get('reason')
        room_number = request.POST.get('room_number')
        bed_number = request.POST.get('bed_number')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')
        due = request.POST.get('due')

        # Create Leave instance
        leave = Leave.objects.create(
            user=user,
            contact_number=contact_number,
            reason=reason,
            room_number=room_number,
            bed_number=bed_number,
            start_date=start_date,
            end_date=end_date,
            due=due
        )

        # Optionally, you can perform validation or additional processing here

        message = 'Your leave application has been submitted successfully.'

    return render(request, 'leave_request.html', {'message': message})  # Render the leave request form with message



def admin_leave_requests(request):
    leave_requests = Leave.objects.all()
    return render(request, 'admin_leave_requests.html', {'leave_requests': leave_requests})




def my_leave_requests(request):
    # Get leave requests of the current user
    leave_requests = Leave.objects.filter(user=request.user)
    return render(request, 'my_leave_requests.html', {'leave_requests': leave_requests})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Leave

def update_leave_request(request, leave_id):
    leave_request = get_object_or_404(Leave, id=leave_id)
    if leave_request.user == request.user:
        if request.method == 'POST':
            leave_request.reason = request.POST.get('reason')
            leave_request.room_number = request.POST.get('room_number')
            leave_request.start_date = request.POST.get('start_date')
            leave_request.end_date = request.POST.get('end_date')
            leave_request.description = request.POST.get('description')
            leave_request.save()
            return redirect('my_leave_requests')
        return render(request, 'leave_request_update.html', {'leave_request': leave_request})
    return redirect('my_leave_requests')

def delete_leave_request(request, leave_id):
    leave_request = get_object_or_404(Leave, id=leave_id)
    if leave_request.user == request.user:
        leave_request.delete()
    return redirect('my_leave_requests')
