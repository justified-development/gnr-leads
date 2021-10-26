from django.contrib import admin
from .models import Lead, Account, Message

# Register your models here.
admin.site.register(Lead)
admin.site.register(Account)
admin.site.register(Message)