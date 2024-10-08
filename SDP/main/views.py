from django.shortcuts import redirect, render
from .models import SeniorDesign
from .forms import SeniorDesignForm

# Create your views here.

def main(request):
    senior_designs = SeniorDesign.objects.all()
    return render(request, 'main_page.html', {'senior_designs': senior_designs})

def new_team_entry(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new team entry to the database
            return redirect('main')  # Redirect back to the main page after submission
    else:
        form = SeniorDesignForm()

    return render(request, 'new_team_entry.html', {'form': form})