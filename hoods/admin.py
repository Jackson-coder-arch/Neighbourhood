from django.contrib import admin
from .models import NeighbourHood,User,Business,Account, MyAccountManager
# Register your models here.

class NeighbourHood(admin.ModelAdmin):
    search_fields =['name','loxation','photo','counts','created_by']

class User(admin.ModelAdmin):
    list_display =('user')

class Business(admin.ModelAdmin):
    search_fields = ['name','neighbourhood','description','business_photo','created_by']

class Account(admin.ModelAdmin):
    list_display=('email','username')

