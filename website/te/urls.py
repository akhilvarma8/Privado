from django.urls import path

from . import views

urlpatterns = [
    path('customer/<customer_id>/templates', views.customer_templates, name='customer_templates'),
    path('system/templates', views.system_templates, name='system_templates'),
    path('reset', views.reset_templates, name='reset_templates'),
]
