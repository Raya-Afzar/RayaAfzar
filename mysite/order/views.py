# order/views.py

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import random
import base64
from num2words import num2words
from captcha.image import ImageCaptcha
from django.views.decorators.csrf import csrf_exempt

# handmade
from mysite.order.models import OrderModel
from mysite.order.forms import OrderForm


@csrf_exempt
def InitCaptcha(request):
    RandNumber = random.randint(1111,9999)
    request.session["captcha"] = RandNumber
    request.session.modified = True
    image = ImageCaptcha(width = 280, height = 90)
    data = image.generate(str(RandNumber)) 
    encoded_string = base64.b64encode(data.getvalue())

    cleaned_data = encoded_string.decode('utf-8')
    return HttpResponse(cleaned_data)




class OrderCreateView(CreateView):

    model = OrderModel
    form_class = OrderForm
    template_name = 'order/order-create.html'
    success_url = reverse_lazy('order:order_success')

    def form_valid(self, form):
        captcha_value = self.request.POST.get('captcha')
        if not captcha_value.isnumeric():
            return render(self.request, 'company/contact-us.html', {'error_message': 'کپچا اشتباه است', 'form':self.form_class})

        if int(captcha_value) == self.request.session["captcha"]:
            self.request.session["captcha"] = None
            types = self.request.POST.getlist('type')
            self.object = form.save()
            self.object.type = "-".join(types)
            self.object.save()
            return super().form_valid(form)
        else:
            return render(self.request, 'order/order-create.html', {'error_message': 'کپچا اشتباه است', 'form':self.form_class})


class OrderSuccessView(TemplateView):

    template_name =  'order/order-success.html'


class CheckedOrderListView(LoginRequiredMixin, ListView):

    template_name = 'order/checked-order-list.html'
    model = OrderModel
    context_object_name = 'order_list'

    def get_queryset(self, *args, **kwargs):

        query_set = super().get_queryset(*args)
        query_set = query_set.filter(checked = True)
        return query_set



class UnCheckedOrderListView(LoginRequiredMixin, ListView):

    template_name = 'order/unchecked-order-list.html'
    model = OrderModel
    context_object_name = 'order_list'

    def get_queryset(self, *args, **kwargs):

        query_set = super().get_queryset(*args)
        query_set = query_set.filter(checked = False)
        return query_set


@login_required
def OrderCheckView(request, pk):

    order = OrderModel.objects.get(pk = pk)
    order.checked = True
    order.save()

    return HttpResponseRedirect(reverse('order:unchecked_order_list'))


class OrderDeleteView(LoginRequiredMixin, DeleteView):

    model = OrderModel
    template_name = 'order/order-delete.html'
    success_url = reverse_lazy('order:checked_order_list')
