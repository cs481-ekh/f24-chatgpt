from django import forms
from .models import SeniorDesign, Student, Sponsor

class SeniorDesignForm(forms.ModelForm):
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
