# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


# Create your views here.
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            #profile.user=current_user.id
            profile.save()

        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/profile-form.html', {"form":form})
def profile(request):
    #current_user = request.user
    profile = Profile.objects.all()
 
    
    
    return render(request,'profile/profile-view.html',{'profile':profile})