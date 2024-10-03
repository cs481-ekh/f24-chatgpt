# views.py
from django.shortcuts import render, redirect
from .models import login  # Assuming you have a custom Login model
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password exist in the Login model
        try:
            user = login.objects.get(username=username)
            if user.password == password:
                # Redirect to the main page after successful login
                return redirect('')
            else:
                # If password is incorrect, add error message
                messages.error(request, 'Invalid password. Please try again.')
        except login.DoesNotExist:
            # If username does not exist, add error message
            messages.error(request, 'Invalid username. Please try again.')

    return render(request, 'login.html')
