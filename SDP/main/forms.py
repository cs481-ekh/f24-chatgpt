# forms.py
from django import forms
from .models import SeniorDesign, Student, Sponsor
from django.forms import formset_factory

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_first_name', 'student_last_name']

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['sponsor_first_name', 'sponsor_last_name', 'affiliation', 'email']

class SeniorDesignForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False)
    sponsors = forms.ModelMultipleChoiceField(queryset=Sponsor.objects.all(), required=False)

    SEMESTER_YEAR_CHOICES = [
        ('Fall 2024', 'Fall 2024'),
        ('Spring 2025', 'Spring 2025'),
        ('Fall 2025', 'Fall 2025'),
    ]

    semester_year = forms.ChoiceField(choices=SEMESTER_YEAR_CHOICES, required=True, label="Semester/Year")

    DEPARTMENT_CHOICES = [
        ('Civil Engineering', 'Civil Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Computer Systems Engineering', 'Electrical & Computer Engineering'),
        ('Construction Management', 'Construction Management'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Materials Science & Engineering', 'Materials Science & Engineering'),
        ('Mechanical & Biomedical Engineering', 'Mechanical & Biomedical Engineering'),
        ('Cyber Operations and Resilience', 'Cyber Operations and Resilience'),
        ('Engineering PLUS', 'Engineering PLUS'),
    ]

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        required=True,
        label="Department",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SeniorDesign
        fields = [
            'department',
            'semester_year',
            'poster_title',
            'abstract',
            'need_power',
            'need_more',
            'table',
            'easle',
            'foam',
            'special_requirements',
            'additional_comments',
            'sponsor_logos',
            'pictures',
            'ada_compliance',
            'students',
            'sponsors'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].required = False
        self.fields['sponsors'].required = False

StudentFormSet = formset_factory(StudentForm, extra=1)
SponsorFormSet = formset_factory(SponsorForm, extra=1)