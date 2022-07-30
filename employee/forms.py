from django import forms
from employee.models import EmployeeModel

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"