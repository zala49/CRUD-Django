from django.shortcuts import redirect, render
from project.models import ProjectModel
from project.forms import ProjectRegistration
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse, reverse_lazy


# add and show
class ProjectAddShowView(CreateView):
    form_class = ProjectRegistration
    template_name = "project/addandshow.html"
    success_url = "/project/"

class ProjectListView(ListView):
    context_object_name = 'stu'
    model = ProjectModel
    template_name = 'project/projectlist.html'

 # Update/Edit
class UpdateProjectView(UpdateView):
    model = ProjectModel
    form_class = ProjectRegistration
    template_name = 'project/updateproject.html'
    success_url = reverse_lazy('project:projectlist')

# Delete
class ProjectDeleteView(DeleteView):
    model = ProjectModel   
    def get_success_url(self):
        return reverse('project:projectlist')