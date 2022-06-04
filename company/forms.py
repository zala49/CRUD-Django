from django import forms
from company.models import CompanyModel


class CompanyRegistration(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = "__all__"