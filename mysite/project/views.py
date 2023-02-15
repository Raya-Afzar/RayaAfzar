# project/views.py

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from mysite.project.models import ProjectModel
from mysite.project.forms import ProjectForm



class ProjectCreateView(CreateView):

    model = ProjectModel
    form_class = ProjectForm
    template_name = 'project/project-create.html'
    success_url = reverse_lazy('account:dashboard')

    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)


class ProjectListView(ListView):

    context_object_name = 'project_list'
    model = ProjectModel
    template_name = 'project/project-list.html'


class ProjectDetailView(DetailView):

    context_object_name = 'project'
    model = ProjectModel
    template_name = 'project/project-detail.html'


class ProjectDeleteView(LoginRequiredMixin, DeleteView):

    model = ProjectModel
    template_name = 'project/project-delete.html'
    success_url = reverse_lazy('project:list')
