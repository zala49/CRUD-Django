from django.contrib import admin
from company.models import CompanyModel

@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ['pk']
    list_display = ['id', 'company', 'email', 'address']
