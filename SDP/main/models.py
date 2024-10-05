from django.db import models

# Create your models here.

class SeniorDesign(models.Model):
    Team_abbreviation = models.CharField(max_length=4)
    Location = models.CharField(max_length=100)
    Poster_tittle = models.CharField(max_length=100)
    Abstract = models.TextField()
    num_team_members = models.IntegerField()
    team_member_names = models.CharField(max_length=100)
    Need_power = models.BooleanField(default=False)
    two_outlets = models.BooleanField(default=False)
    table = models.BooleanField(default=False)
    foamboard = models.BooleanField(default=False)
    clips = models.BooleanField(default=False)
    large_presentaion = models.BooleanField(default=False)
    sponsor_logos = models.BooleanField(default=False)
    picutures = models.BooleanField(default=False)

    def __str__(self):
        return self.Team_abbreviation