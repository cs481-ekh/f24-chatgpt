from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.main, name='main'),  # Main page
    path('', views.senior_design_list, name='project_list'),
    path('admin/', admin.site.urls),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('new/', views.new_team_entry, name='new_team_entry'),  # New team entry form
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Edit team entry form
    path('delete/<int:entry_id>/', views.delete_team_entry, name='delete_team_entry'),
]

print("URL Patterns loaded:", urlpatterns)  # Debug print


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)