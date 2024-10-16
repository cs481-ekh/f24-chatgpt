from django.shortcuts import redirect, render
from .models import SeniorDesign
from .forms import SeniorDesignForm


# Create your views here.

def main(request):
    senior_designs = SeniorDesign.objects.all()
    return render(request, 'main-page.component.html', {'senior_designs': senior_designs})

def new_team_entry(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new team entry to the database
            return redirect('main')  # Redirect back to the main page after submission
    else:
        form = SeniorDesignForm()

    return render(request, 'new-team-entry.component.html', {'form': form})

def create_senior_design(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = SeniorDesignForm()
    return render(request, 'create_senior_design.html', {'form': form})

def senior_design_list(request):
    designs = SeniorDesign.objects.all()
    return render(request, 'senior_design_list.html', {'designs': designs})