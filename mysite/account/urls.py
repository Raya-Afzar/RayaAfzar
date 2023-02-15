from django.urls import include, path
from django.contrib.auth import views as auth_views

from mysite.account.forms import UserLoginForm
from mysite.account.views import SuperuserDashboardView

app_name ='account'
urlpatterns = [
    path('dashboard/',SuperuserDashboardView.as_view(), name='dashboard'),
    path('auth/',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=UserLoginForm), name='login'),

]
