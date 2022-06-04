from django import forms
from project.models import ProjectModel


class ProjectRegistration(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = "__all__"