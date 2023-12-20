# order/urls.py

from django.urls import include, path
from django.contrib.auth import views as auth_views

from mysite.order.views import (OrderCreateView, OrderSuccessView,
            CheckedOrderListView, UnCheckedOrderListView, OrderCheckView,
            OrderDeleteView,InitCaptcha)

app_name ='order'
urlpatterns = [
    path('order-create/',OrderCreateView.as_view(), name='order_create'),
    path('checked-order-list/',CheckedOrderListView.as_view(), name='checked_order_list'),
    path('unchecked-order-list/', UnCheckedOrderListView.as_view(), name='unchecked_order_list'),
    path('order-success/',OrderSuccessView.as_view(), name='order_success'),
    path('order-check/<int:pk>/',OrderCheckView, name='order_check'),
    path('order-delete/<int:pk>/',OrderDeleteView.as_view(), name='order_delete'),
    path('create-captcha/',InitCaptcha, name='captcha'),

]
