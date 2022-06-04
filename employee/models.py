from django.db import models
from project.models import ProjectModel
from department.models import DepartmentModel
from company.models import CompanyModel

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.ForeignKey(CompanyModel,on_delete=models.CASCADE, null=True, blank=True)
    department_name = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True, blank=True)
    project_name = models.ForeignKey(ProjectModel,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(self.project_name)