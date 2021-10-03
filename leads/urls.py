from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
  path('', views.index, name='index')
]