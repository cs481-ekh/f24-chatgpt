from django import forms
from .models import SeniorDesign

class SeniorDesignForm(forms.ModelForm):
    class Meta:
        model = SeniorDesign
        fields = ['Team_abbreviation', 'Location', 'Poster_title', 'Abstract', 'num_team_members', 'team_member_names', 
                  'Need_power', 'two_outlets', 'table', 'foamboard', 'clips', 'large_presentation', 
                  'sponsor_logos', 'sponsor_logo_image', 'pictures', 'project_picture']
        widgets = {
            'sponsor_logo_image': forms.ClearableFileInput(attrs={'multiple': False}),
            'project_picture': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def clean(self):
        cleaned_data = super().clean()
        sponsor_logos = cleaned_data.get('sponsor_logos')
        sponsor_logo_image = cleaned_data.get('sponsor_logo_image')
        pictures = cleaned_data.get('pictures')
        project_picture = cleaned_data.get('project_picture')

        if sponsor_logos and not sponsor_logo_image:
            self.add_error('sponsor_logo_image', 'Please upload a sponsor logo image.')
        if pictures and not project_picture:
            self.add_error('project_picture', 'Please upload a project picture.')

        return cleaned_data