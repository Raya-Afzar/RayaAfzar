# comment/urls.py

from django.urls import include, path
from django.contrib.auth import views as auth_views

from mysite.comment.views import (CommentCreateView, CommentListView, CommentDeleteView,
                    FamousCustomerCreateView, FamousCustomerListView, FamousCustomerDeleteView)

app_name ='comment'
urlpatterns = [
    path('comment-create/',CommentCreateView.as_view(), name='comment_create'),
    path('comment-list/',CommentListView.as_view(), name='comment_list'),
    path('comment-delete/<int:pk>/',CommentDeleteView.as_view(), name='comment_delete'),
    path('famous-customer-create/',FamousCustomerCreateView.as_view(), name='famous_customer_create'),
    path('famous-customer-list/',FamousCustomerListView.as_view(), name='famous_customer_list'),
    path('famous-customer-delete/<int:pk>/',FamousCustomerDeleteView.as_view(), name='famous_customer_delete'),

]
