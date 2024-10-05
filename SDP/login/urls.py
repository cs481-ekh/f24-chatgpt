from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
  path('', views.login_view, name='login'),
  path('login/', views.login_view, name='login'),
]

'''
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('admin/', admin.site.urls),
'''