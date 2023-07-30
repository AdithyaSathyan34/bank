from django.contrib import admin

# Register your models here.

INSTALLED_APPS = [

    'bankingapp',
]

from django.contrib import admin
from .models import bank_detail  # Import your model here

admin.site.register(bank_detail)  # Register your model with the admin site