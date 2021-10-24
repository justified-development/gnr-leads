from django.http import HttpResponse
from django.core.mail import send_mail
from models import Lead
from django.shortcuts import render   

# Create your views here.


def html_table(request, date):    
    content = Lead.objects.filter(created_date =date)
    return render(request, 'email.html', {'content': content})


