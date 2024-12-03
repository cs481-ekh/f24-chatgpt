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
    
    # Add student names to each senior design project
    for design in senior_designs:
        design.team_member_names = ", ".join(
            f"{student.student_first_name} {student.student_last_name}" 
            for student in design.students.all()
        )
        design.sponsor_names = ", ".join(
            f"{sponsor.sponsor_first_name} {sponsor.sponsor_last_name}"
            for sponsor in design.sponsors.all()
        )
    
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
        try:
            # Create the senior design record first
            senior_design = SeniorDesign.objects.create(
                department=request.POST.get('department'),
                semester_year=request.POST.get('semester_year'),
                poster_title=request.POST.get('poster_title'),
                abstract=request.POST.get('abstract'),
                special_requirements=request.POST.get('special_requirements'),
                additional_comments=request.POST.get('additional_comments'),
                need_power=request.POST.get('need_power') == 'on',
                need_more=request.POST.get('need_more') == 'on',
                table=request.POST.get('table') == 'on',
                easle=request.POST.get('easle') == 'on',
                foam=request.POST.get('foam') == 'on',
                sponsor_logos=request.POST.get('sponsor_logos') == 'on',
                pictures=request.POST.get('pictures') == 'on',
                ada_compliance=request.POST.get('ada_compliance') == 'on'
            )

            # Get student data from POST
            student_first_names = request.POST.getlist('student_first_name[]')
            student_last_names = request.POST.getlist('student_last_name[]')
            
            # Create and add students
            for first_name, last_name in zip(student_first_names, student_last_names):
                if first_name and last_name:  # Only create if both names are provided
                    student = Student.objects.create(
                        student_first_name=first_name,
                        student_last_name=last_name
                    )
                    senior_design.students.add(student)

            # Get sponsor data from POST
            sponsor_first_names = request.POST.getlist('sponsor_first_name[]')
            sponsor_last_names = request.POST.getlist('sponsor_last_name[]')
            sponsor_affiliations = request.POST.getlist('affiliation[]')
            sponsor_emails = request.POST.getlist('email[]')
            
            # Create and add sponsors
            for first_name, last_name, affiliation, email in zip(
                sponsor_first_names, sponsor_last_names, 
                sponsor_affiliations, sponsor_emails):
                if all([first_name, last_name, affiliation, email]):  # Only create if all fields are provided
                    sponsor = Sponsor.objects.create(
                        sponsor_first_name=first_name,
                        sponsor_last_name=last_name,
                        affiliation=affiliation,
                        email=email
                    )
                    senior_design.sponsors.add(sponsor)

            return redirect('main')
            
        except Exception as e:
            print(f"Error creating entry: {str(e)}")
            # Re-render the form with the submitted data
            form = SeniorDesignForm(request.POST)
            return render(request, 'new-team-entry.component.html', {
                'form': form,
                'error': str(e)
            })
    else:
        form = SeniorDesignForm()
        
    return render(request, 'new-team-entry.component.html', {
        'form': form
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
    senior_design = get_object_or_404(SeniorDesign, pk=entry_id)
    
    if request.method == 'POST':
        try:
            # Update the senior design record
            senior_design.department = request.POST.get('department')
            senior_design.semester_year = request.POST.get('semester_year')
            senior_design.poster_title = request.POST.get('poster_title')
            senior_design.abstract = request.POST.get('abstract')
            senior_design.special_requirements = request.POST.get('special_requirements')
            senior_design.additional_comments = request.POST.get('additional_comments')
            senior_design.need_power = request.POST.get('need_power') == 'on'
            senior_design.need_more = request.POST.get('need_more') == 'on'
            senior_design.table = request.POST.get('table') == 'on'
            senior_design.easle = request.POST.get('easle') == 'on'
            senior_design.foam = request.POST.get('foam') == 'on'
            senior_design.sponsor_logos = request.POST.get('sponsor_logos') == 'on'
            senior_design.pictures = request.POST.get('pictures') == 'on'
            senior_design.ada_compliance = request.POST.get('ada_compliance') == 'on'
            senior_design.save()

            # Clear existing relationships
            senior_design.students.clear()
            senior_design.sponsors.clear()

            # Get and update student data
            student_first_names = request.POST.getlist('student_first_name[]')
            student_last_names = request.POST.getlist('student_last_name[]')
            
            # Create and add students
            for first_name, last_name in zip(student_first_names, student_last_names):
                if first_name and last_name:  # Only create if both names are provided
                    student = Student.objects.create(
                        student_first_name=first_name,
                        student_last_name=last_name
                    )
                    senior_design.students.add(student)

            # Get and update sponsor data
            sponsor_first_names = request.POST.getlist('sponsor_first_name[]')
            sponsor_last_names = request.POST.getlist('sponsor_last_name[]')
            sponsor_affiliations = request.POST.getlist('affiliation[]')
            sponsor_emails = request.POST.getlist('email[]')
            
            # Create and add sponsors
            for first_name, last_name, affiliation, email in zip(
                sponsor_first_names, sponsor_last_names, 
                sponsor_affiliations, sponsor_emails):
                if all([first_name, last_name, affiliation, email]):  # Only create if all fields are provided
                    sponsor = Sponsor.objects.create(
                        sponsor_first_name=first_name,
                        sponsor_last_name=last_name,
                        affiliation=affiliation,
                        email=email
                    )
                    senior_design.sponsors.add(sponsor)

            return redirect('main')
            
        except Exception as e:
            print(f"Error updating entry: {str(e)}")
            return render(request, 'edit-entry.component.html', {
                'form': SeniorDesignForm(instance=senior_design),
                'entry': senior_design,
                'error': str(e)
            })
    else:
        # Display the form for GET request
        form = SeniorDesignForm(instance=senior_design)
        
    return render(request, 'edit-entry.component.html', {
        'form': form,
        'entry': senior_design,
    })

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
