import imp
from django.db import models
from company.models import CompanyModel

class ProjectModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=500)

    def __str__(self):
        return self.project_name
        