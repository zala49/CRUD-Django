from django.contrib import admin
from department.models import DepartmentModel


@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'company','department_name']
