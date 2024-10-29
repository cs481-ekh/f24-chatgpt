from django.db import models

class SeniorDesign(models.Model):
    Department = models.CharField(max_length=100, default='Department X')
    Poster_title = models.CharField(max_length=255, default='Title')
    Abstract = models.TextField(max_length=900, default='Abstract')
    num_team_members = models.IntegerField(default=1)
    team_member_names = models.TextField(default='Name')
    Need_power = models.BooleanField(default=False)
    Need_more = models.BooleanField(default=False)
    table = models.BooleanField(default=False)
    easle = models.BooleanField(default=False)
    foam = models.BooleanField(default=False)
    Brief_description = models.TextField(max_length=900, default='Abstract')
    Any_additional_comments = models.TextField(max_length=900, default='Abstract')
    sponsor_logos = models.BooleanField(default=False)
    pictures = models.BooleanField(default=False)
    sponsor_first_last_name = models.TextField(default='Name')
    sponsor_affiliation = models.TextField(default='Name')
    contact_email = models.TextField(default='Name')
    

    def __str__(self):
        return self.Team_abbreviation