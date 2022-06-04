from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from department.models import DepartmentModel
from department.forms import DepartmentRegistration
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy

# add and show
class DepartmentAddShowView(CreateView):
    form_class = DepartmentRegistration
    template_name = "department/addandshow.html"
    success_url = "/department/"

class DepartmentListView(ListView):
    context_object_name = 'stu'
    model = DepartmentModel
    template_name = 'department/departmentlist.html'

 # Update/Edit
class UpdateDepartmentView(UpdateView):
    model = DepartmentModel
    form_class = DepartmentRegistration
    template_name = 'department/updatedepartment.html'
    success_url = reverse_lazy('department:departmentlist')

# Delete
class DepartmentDeleteView(DeleteView):
    model = DepartmentModel   
    def get_success_url(self):
        return reverse('department:departmentlist')