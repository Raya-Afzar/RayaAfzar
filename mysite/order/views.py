# order/views.py

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# handmade
from mysite.order.models import OrderModel
from mysite.order.forms import OrderForm


class OrderCreateView(CreateView):

    model = OrderModel
    form_class = OrderForm
    template_name = 'order/order-create.html'
    success_url = reverse_lazy('order:order_success')

    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)


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
