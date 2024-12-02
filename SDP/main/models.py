from django.db import models

class Student(models.Model):
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_first_name} {self.student_last_name}"

    objects = models.Manager()

class Sponsor(models.Model):
    sponsor_first_name = models.CharField(max_length=100)
    sponsor_last_name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.sponsor_first_name} {self.sponsor_last_name}"

    objects = models.Manager()

class SeniorDesign(models.Model):
    department = models.CharField(max_length=100, default='Department')
    semester_year = models.CharField(max_length=100, default='Semester Year')
    poster_title = models.CharField(max_length=255,default='Poster Title')
    abstract = models.TextField(max_length=900, default='Abstract')
    need_power = models.BooleanField(default=False)
    need_more = models.BooleanField(default=False)
    table = models.BooleanField(default=False)
    easle = models.BooleanField(default=False)
    foam = models.BooleanField(default=False)
    special_requirements = models.TextField(max_length=900, blank=True)
    additional_comments = models.TextField(max_length=900, blank=True)
    sponsor_logos = models.BooleanField(default=False)
    pictures = models.BooleanField(default=False)
    ada_compliance = models.BooleanField(default=False)

    students = models.ManyToManyField(Student, related_name='senior_design_projects')
    sponsors = models.ManyToManyField(Sponsor, related_name='sponsored_projects')

    def __str__(self):
        return self.poster_title
