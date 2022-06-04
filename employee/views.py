from django.shortcuts import redirect, render
from employee.models import EmployeeModel
from employee.forms import EmployeeRegistration
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

# add and show
class EmployeeAddShowView(CreateView):
    form_class = EmployeeRegistration
    template_name = "employee/addandshow.html"
    success_url = "/employee/"

class EmployeeListView(ListView):
    context_object_name = 'stu'
    model = EmployeeModel
    template_name = 'employee/employeelist.html'

 # Update/Edit
class UpdateEmployeeView(UpdateView):
    model = EmployeeModel
    form_class = EmployeeRegistration
    template_name = 'employee/updateemployee.html'
    success_url = reverse_lazy('employee:employeelist')

# Delete
class EmployeeDeleteView(DeleteView):
    model = EmployeeModel
    def get_success_url(self):
        return reverse('employee:employeelist')

