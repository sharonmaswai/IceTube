from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Rating


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','profile_pic', 'specialisation','county') 
class RateForm(forms.ModelForm):
    class Meta:
        model= Rating
        fields= ('rating',)        

