from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SeniorDesign, Student, Sponsor
from .forms import SeniorDesignForm, StudentFormSet, SponsorFormSet
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
        'Number of Students',
        'Student Names',
        'Need Power',
        'Need More',
        'Table',
        'Easel',
        'Foam Board',
        'Special Requirements',
        'Additional Comments',
        'Sponsor Logos',
        'Pictures',
        'ADA Compliance',
        'Sponsors'
    ])
    
    senior_designs = SeniorDesign.objects.all()
    for design in senior_designs:
        # Get student names
        student_names = ", ".join(str(student) for student in design.students.all())
        # Get sponsor names
        sponsor_names = ", ".join(str(sponsor) for sponsor in design.sponsors.all())
        
        writer.writerow([
            design.department,
            design.semester_year,
            design.poster_title,
            design.abstract,
            design.students.count(),
            student_names,
            'Yes' if design.need_power else 'No',
            'Yes' if design.need_more else 'No',
            'Yes' if design.table else 'No',
            'Yes' if design.easle else 'No',
            'Yes' if design.foam else 'No',
            design.special_requirements,
            design.additional_comments,
            'Yes' if design.sponsor_logos else 'No',
            'Yes' if design.pictures else 'No',
            'Yes' if design.ada_compliance else 'No',
            sponsor_names
        ])

    return response

@login_required
@user_passes_test(is_user)
def new_team_entry(request):
    if request.method == 'POST':
        form = SeniorDesignForm(request.POST)
        student_formset = StudentFormSet(request.POST, prefix='student')
        sponsor_formset = SponsorFormSet(request.POST, prefix='sponsor')
        
        print("Form valid:", form.is_valid())
        print("Student formset valid:", student_formset.is_valid())
        print("Sponsor formset valid:", sponsor_formset.is_valid())
        
        if student_formset.is_valid() and sponsor_formset.is_valid():
            try:
                # First save the formsets to create Student and Sponsor instances
                students = []
                sponsors = []
                
                # Save students
                for student_form in student_formset:
                    if student_form.cleaned_data and not student_form.cleaned_data.get('DELETE', False):
                        student = student_form.save()
                        students.append(student.id)
                
                # Save sponsors
                for sponsor_form in sponsor_formset:
                    if sponsor_form.cleaned_data and not sponsor_form.cleaned_data.get('DELETE', False):
                        sponsor = sponsor_form.save()
                        sponsors.append(sponsor.id)
                
                # Now add the students and sponsors to the POST data
                post_data = request.POST.copy()
                post_data.setlist('students', students)
                post_data.setlist('sponsors', sponsors)
                
                # Create form with updated POST data
                form = SeniorDesignForm(post_data)
                
                if form.is_valid():
                    senior_design = form.save()
                    return redirect('main')
                else:
                    print("Form errors:", form.errors)
                    
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print("Student formset errors:", student_formset.errors)
            print("Sponsor formset errors:", sponsor_formset.errors)
    else:
        form = SeniorDesignForm()
        student_formset = StudentFormSet(prefix='student')
        sponsor_formset = SponsorFormSet(prefix='sponsor')

    return render(request, 'new-team-entry.component.html', {
        'form': form,
        'student_formset': student_formset,
        'sponsor_formset': sponsor_formset,
    })


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
