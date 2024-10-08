from django import forms
from .models import SeniorDesign

class SeniorDesignForm(forms.ModelForm):
    class Meta:
        model = SeniorDesign
        fields = ['Team_abbreviation', 'Location', 'Poster_title', 'Abstract', 'num_team_members', 'team_member_names', 
                  'Need_power', 'two_outlets', 'table', 'foamboard', 'clips', 'large_presentation', 'sponsor_logos', 'pictures']
