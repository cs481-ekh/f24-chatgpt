from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import SeniorDesign
from .forms import SeniorDesignForm
from django import get_object_or_404


def is_user(user):
    return user.groups.filter(name='User').exists()

def is_planner(user):
    return user.groups.filter(name='Planner').exists()

# Create your views here.
def main(request):
    senior_designs = SeniorDesign.objects.all()

    is_planner = request.user.groups.filter(name='Planner').exists()

    return render(request, 'main-page.component.html', {
        'senior_designs': senior_designs,
        'is_planner': is_planner})

@login_required
@user_passes_test(is_user)
def new_team_entry(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new team entry to the database
            return redirect('main')  # Redirect back to the main page after submission
    else:
        form = SeniorDesignForm()

    return render(request, 'new-team-entry.component.html', {'form': form})

@login_required
@user_passes_test(is_user)
def create_senior_design(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = SeniorDesignForm()
    return render(request, 'create_senior_design.html', {'form': form})

@login_required
@user_passes_test(is_user)
def edit_entry(request, entry_id):
    entry = get_object_or_404(SeniorDesign, pk=entry_id)
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = SeniorDesignForm(instance=entry)

    return render(request, 'edit-entry.component.html', {'form': form, 'entry': entry})


@login_required
def senior_design_list(request):
    designs = SeniorDesign.objects.all()
    return render(request, 'senior_design_list.html', {'designs': designs})