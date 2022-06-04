from django import forms
from department.models import DepartmentModel

class DepartmentRegistration(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields = "__all__"