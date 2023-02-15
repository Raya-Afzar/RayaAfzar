from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Handmade
from mysite.account.decorators import superuser_required

class SuperuserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/superuserdashboard.html'
