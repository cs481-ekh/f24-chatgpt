from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.main, name='main'),  # Main page
    path('new/', views.new_team_entry, name='new_team_entry'),  # New team entry form
    path('', views.senior_design_list, name='project_list'),
    path('admin/', admin.site.urls),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Edit team entry form
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)