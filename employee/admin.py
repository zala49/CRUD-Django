from django.contrib import admin
from employee.models import EmployeeModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','company', 'email', 'project_name','department_name' ]
