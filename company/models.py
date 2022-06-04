from django.db import models

class CompanyModel(models.Model):
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.company