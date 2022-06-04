from django.db import models
from company.models import CompanyModel

class DepartmentModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    department_name = models.CharField(max_length=250, unique=True)
    
    def __str__(self):
        return self.department_name
        