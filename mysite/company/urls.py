# company/urls.py

from django.urls import include, path
from django.contrib.auth import views as auth_views

from mysite.company.views import (ContactUsCreateView, ContactUsListView,
            ContactUsDeleteView, ContactUsSuccessView, PricingView,
            FAQsView, AboutUsView, WebDevelopmentServiceView,
            ProgrammingServiceView,)

app_name ='company'
urlpatterns = [
    path('contact-us/',ContactUsCreateView.as_view(), name='contact_us'),
    path('contact-us-list/',ContactUsListView.as_view(), name='contact_us_list'),
    path('contact-us-delete/<int:pk>/',ContactUsDeleteView.as_view(), name='contact_us_delete'),
    path('contact-us-success/',ContactUsSuccessView.as_view(), name='contact_us_success'),
    path('about-us/',AboutUsView.as_view(), name='about_us'),
    path('FAQs/',FAQsView.as_view(), name='FAQs'),
    path('pricing/',PricingView.as_view(), name='pricing'),
    path('web-development-service/',WebDevelopmentServiceView.as_view(), name='webdevelopmentservice'),
    path('programming-service/',ProgrammingServiceView.as_view(), name='programmingservice'),

]
