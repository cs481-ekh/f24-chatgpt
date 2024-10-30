from django import forms
from .models import SeniorDesign

class SeniorDesignForm(forms.ModelForm):
    class Meta:
        model = SeniorDesign
        fields = [
            'Department',
            'Semester_Year',
            'Poster_title',
            'Abstract',
            'num_team_members',
            'team_member_names',
            'Need_power',
            'Need_more',
            'table',
            'easle',
            'foam',
            'Brief_description',
            'Any_additional_comments',
            'sponsor_logos',
            'pictures',
            'sponsor_first_last_name',
            'sponsor_affiliation',
            'contact_email'
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data