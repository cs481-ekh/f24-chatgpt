from django.shortcuts import render
from .models import SeniorDesign

# Create your views here.

def main(request):
    senior_designs = SeniorDesign.objects.all()
    return render(request, 'main_page.html', {'senior_designs': senior_designs})