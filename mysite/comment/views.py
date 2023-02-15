# comment/views.py

from django.shortcuts import render
from django.views.generic import DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# handmade
from mysite.comment.models import CommentModel, FamousCustomerModel
from mysite.comment.forms import CommentForm, FamousCustomerForm


class CommentCreateView(CreateView):

    model = CommentModel
    form_class = CommentForm
    template_name = 'comment/comment-create.html'
    success_url = reverse_lazy('account:dashboard')

    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)


class CommentListView(LoginRequiredMixin, ListView):

    context_object_name = 'comment_list'
    model = CommentModel
    template_name = 'comment/comment-list.html'


class CommentDeleteView(LoginRequiredMixin, DeleteView):

    model = CommentModel
    template_name = 'comment/comment-delete.html'
    success_url = reverse_lazy('comment:comment_list')



class FamousCustomerCreateView(CreateView):

    model = FamousCustomerModel
    form_class = FamousCustomerForm
    template_name = 'comment/famous-customer-create.html'
    success_url = reverse_lazy('account:dashboard')

    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)


class FamousCustomerListView(LoginRequiredMixin, ListView):

    context_object_name = 'famous_customer_list'
    model = FamousCustomerModel
    template_name = 'comment/famous-customer-list.html'


class FamousCustomerDeleteView(LoginRequiredMixin, DeleteView):

    model = FamousCustomerModel
    template_name = 'comment/famous-customer-delete.html'
    success_url = reverse_lazy('comment:famous_customer_list')
