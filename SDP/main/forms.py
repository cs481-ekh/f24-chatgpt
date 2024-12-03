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