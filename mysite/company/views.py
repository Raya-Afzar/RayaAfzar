# company/views.py

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from mysite.company.models import ContactUsModel
from mysite.company.forms import ContactUsForm



class ContactUsCreateView(CreateView):

    model = ContactUsModel
    form_class = ContactUsForm
    template_name = 'company/contact-us.html'
    success_url = reverse_lazy('company:contact_us_success')

    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)


class ContactUsListView(LoginRequiredMixin, ListView):

    context_object_name = 'contact_us_list'
    model = ContactUsModel
    template_name = 'company/contact-us-list.html'


class ContactUsDeleteView(LoginRequiredMixin, DeleteView):

    model = ContactUsModel
    template_name = 'company/contact-us-delete.html'
    success_url = reverse_lazy('company:contact_us_list')


class ContactUsSuccessView(TemplateView):
    template_name = 'company/contact-us-success.html'


class PricingView(TemplateView):
    template_name = 'company/pricing.html'


class AboutUsView(TemplateView):
    template_name = 'company/about-us.html'


class FAQsView(TemplateView):
    template_name = 'company/FAQs.html'


class ProgrammingServiceView(TemplateView):
    template_name = 'company/programming-service.html'


class WebDevelopmentServiceView(TemplateView):
    template_name = 'company/web-development-service.html'
