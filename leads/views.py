from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
  return HttpResponse('Brandon, Heidi says your code is trash')


def email_view(request):
  return HttpResponse("where to start???")

def sendSimpleEmail(request,emailto):
   res = send_mail("Today's Angie List", "all_records", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)

   #need to edit project settings & URL???