from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name='main'),
]
'''
  path('main_page', views.main_page, name='main_page'),
  path('admin/', admin.site.urls)
'''