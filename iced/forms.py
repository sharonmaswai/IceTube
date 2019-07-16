from django import forms
from .models import Profile, Rating




        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','task','bio','profile_pic') 
class RateForm(forms.ModelForm):
    class Meta:
        model= Rating
        fields= ('rating',)        