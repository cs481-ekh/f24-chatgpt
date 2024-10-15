from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Login  # Adjust if your model name is different

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = Login.objects.get(username=username)
            if user.password == password:  
                return redirect('main')  # Redirect to main page using the URL pattern name
            else:
                messages.error(request, "Incorrect password.")
        except Login.DoesNotExist:
            messages.error(request, "Username does not exist.")
    
    return render(request, 'login.component.html')
