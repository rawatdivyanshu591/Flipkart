from django.contrib import admin
from django.urls import path,include
from customer.views import*
urlspatterns=[
    path('get-customers',GetCustomerView.as_view())
    path('get-customer',GetCustomerAddressView.as_view())
]