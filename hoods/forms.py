from django import forms
from django.forms import ModelForm
from .models import NeighbourHood, Business, Profile, Posts

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields =('name','location','photo')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','profile_photo','email','estate')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name','description','business_photo','location')

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','post','user','estate')
