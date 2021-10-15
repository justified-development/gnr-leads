from django.urls import path

from leads.services.email_data import Email
from . import views
from django.conf.urls import patterns, url

app_name = 'leads'


urlpatterns = [
  path('', views.index, name='index'),
  path('/email_view/', views.email_view, name = 'email_view'),
]