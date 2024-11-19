from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SeniorDesign
from .forms import SeniorDesignForm
from django.http import HttpResponse
import csv

def is_user(user):
    return user.groups.filter(name='User').exists()

def is_planner(user):
    return user.groups.filter(name='Planner').exists()

def main(request):
    senior_designs = SeniorDesign.objects.all()
    is_planner = request.user.groups.filter(name='Planner').exists()
    return render(request, 'main-page.component.html', {
        'senior_designs': senior_designs,
        'is_planner': is_planner
    })

@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="senior_designs.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Department',
        'Semester/Year',
        'Poster Title',
        'Abstract',
        'Number of Team Members',
        'Team Member Names',
        'Need Power',
        'Need More',
        'Table',
        'Easel',
        'Foam Board',
        'special_requirements',
        'Additional Comments',
        'Sponsor Logos',
        'Pictures',
        'Sponsor First/Last Name',
        'Sponsor Affiliation',
        'Contact Email'
    ])

    senior_designs = SeniorDesign.objects.all()
    for design in senior_designs:
        writer.writerow([
            design.Department,
            design.Semester_Year,
            design.Poster_title,
            design.Abstract,
            design.num_team_members,
            design.team_member_names,
            'Yes' if design.Need_power else 'No',
            'Yes' if design.Need_more else 'No',
            'Yes' if design.table else 'No',
            'Yes' if design.easle else 'No',
            'Yes' if design.foam else 'No',
            design.special_requirements,
            design.Any_additional_comments,
            'Yes' if design.sponsor_logos else 'No',
            'Yes' if design.pictures else 'No',
            design.sponsor_first_last_name,
            design.sponsor_affiliation,
            design.contact_email
        ])

    return response

@login_required
@user_passes_test(is_user)
def new_team_entry(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
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
@user_passes_test(is_user)
def delete_team_entry(request, entry_id):
    senior_design = get_object_or_404(SeniorDesign, id=entry_id)

    if request.method == 'POST':
        senior_design.delete()
        return redirect('main')

    return render(request, 'delete.component.html', {'senior_design': senior_design})

@login_required
def senior_design_list(request):
    designs = SeniorDesign.objects.all()
    return render(request, 'senior_design_list.html', {'designs': designs})
