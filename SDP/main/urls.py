from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Main page
    path('new/', views.new_team_entry, name='new_team_entry'),  # New team entry form
]
