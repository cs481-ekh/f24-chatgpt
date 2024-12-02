from django import forms
from .models import SeniorDesign, Student, Sponsor
from django.forms import formset_factory


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['sponsor_first_name', 'sponsor_last_name', 'affiliation', 'email']

SponsorFormSet = formset_factory(SponsorForm, extra=0)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_first_name', 'student_last_name']


StudentFormSet = formset_factory(StudentForm, extra=0)

class SeniorDesignForm(forms.ModelForm):

    SEMESTER_YEAR_CHOICES = [
        ('fall_2024', 'Fall 2024'),
        ('spring_2025', 'Spring 2025'),
        ('fall_2025', 'Fall 2025'),
    ]

    semester_year = forms.ChoiceField(choices=SEMESTER_YEAR_CHOICES, required=True, label="Semester/Year")

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
            'sponsors',
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        # Add any custom validation logic if needed
        return cleaned_data
