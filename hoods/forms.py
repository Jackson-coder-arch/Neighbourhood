from django import forms
from django.forms import ModelForm
from .models import NeighbourHood, Business, Profile, Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        fields = ('title','post',)

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
