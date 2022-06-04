from multiprocessing import context
from re import template
from django.http import JsonResponse
from django.shortcuts import render, redirect
from company.models import CompanyModel
from company.forms import CompanyRegistration
from django.views.generic import DeleteView, CreateView, ListView, UpdateView
from django.urls import reverse, reverse_lazy

# add and show
class CompanyAddShowView(CreateView):
    form_class = CompanyRegistration
    template_name = "company/addandshow.html"
    success_url = "/company/"

class CompanyListView(ListView):
    context_object_name = 'stu'
    model = CompanyModel
    template_name = 'company/companylist.html'

 # Update/Edit
class UpdateCompanyView(UpdateView):
    model = CompanyModel
    form_class = CompanyRegistration
    template_name = 'company/updatecompany.html'
    success_url = reverse_lazy('company:companylist')

# Delete
class CompanyDeleteView(DeleteView):
    model = CompanyModel   
    def get_success_url(self):
        return reverse('company:companylist')

