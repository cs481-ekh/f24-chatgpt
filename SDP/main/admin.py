from django.contrib import admin
from .models import SeniorDesign
from .models import Student
from .models import Sponsor

# Register your models here.
admin.site.register(SeniorDesign)
admin.site.register(Student)
admin.site.register(Sponsor)