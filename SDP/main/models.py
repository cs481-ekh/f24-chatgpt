from django.db import models

class SeniorDesign(models.Model):
    Team_abbreviation = models.CharField(max_length=100, default='Team')
    Location = models.CharField(max_length=100, default='Location')
    Poster_title = models.CharField(max_length=255, default='Title')
    Abstract = models.TextField(default='Abstract')
    num_team_members = models.IntegerField(default=1)
    team_member_names = models.TextField(default='Name')
    Need_power = models.BooleanField(default=False)
    two_outlets = models.BooleanField(default=False)
    table = models.BooleanField(default=False)
    foamboard = models.BooleanField(default=False)
    clips = models.BooleanField(default=False)
    large_presentation = models.BooleanField(default=False)
    sponsor_logos = models.BooleanField(default=False)
    sponsor_logo_image = models.ImageField(upload_to='sponsor_logos/', blank=True, null=True)
    pictures = models.BooleanField(default=False)
    project_picture = models.ImageField(upload_to='project_pictures/', blank=True, null=True)

    def __str__(self):
        return self.Team_abbreviation