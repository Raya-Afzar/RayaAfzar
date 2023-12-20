# company/views.py

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from mysite.company.models import ContactUsModel
from mysite.company.forms import ContactUsForm
from mysite.order.views import InitCaptcha



class ContactUsCreateView(CreateView):

    model = ContactUsModel
    form_class = ContactUsForm
    template_name = 'company/contact-us.html'
    success_url = reverse_lazy('company:contact_us_success')

    def form_valid(self, form):
        captcha_value = self.request.POST.get('captcha')
        if not captcha_value.isnumeric():
            return render(self.request, 'company/contact-us.html', {'error_message': 'کپچا اشتباه است', 'form':self.form_class})

        if int(captcha_value) == self.request.session["captcha"]:
            self.request.session["captcha"] = None
                
            self.object = form.save()
            return super().form_valid(form)
        else:
            return render(self.request, 'company/contact-us.html', {'error_message': 'کپچا اشتباه است', 'form':self.form_class})


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
