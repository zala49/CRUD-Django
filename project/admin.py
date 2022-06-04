from django.contrib import admin
from project.models import ProjectModel


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'company','project_name', 'project_description']
