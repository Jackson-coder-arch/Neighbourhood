from django.contrib import admin
from .models import NeighbourHood,User,Business,Profile

@admin.register(NeighbourHood)
class NeighbourHood(admin.ModelAdmin):
    search_fields =['name','location','photo','counts','created_by']
    
    class Meta:
        model = NeighbourHood

# @admin.register(User)
# class User(admin.ModelAdmin):
#     list_display =('user',)

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    search_fields=['user','profile_photo','email']

    class Meta:
        model = Profile

@admin.register(Business)
class Business(admin.ModelAdmin):
    search_fields = ['name','neighbourhood','description','business_photo','created_by']

    class Meta:
        model = Business

# @admin.register(Account)
# class Account(admin.ModelAdmin):
#     list_display=['email','username',]

#     class Meta:
#         model = Account

