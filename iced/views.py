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
    current_user = request.user
   
    profiles=Profile.objects.filter(id=profile_id)
    ratings=Rating.objects.filter(profile_id=profiles)
    average_rating=[]
    mean_rate=0 
        
    for rate in ratings:
        average_rating.append(rate.rating)
            
    total_rates=sum(average_rating)
    if len(ratings)>0:
        total_rating=total_rates/len(ratings)
        mean_rate=total_rating
    else:
        total_rating=0
        mean_rate=total_rating  
    
    
    return render(request,'profile/profile-view.html',{'profile':profile, 'ratings':ratings})
def rate(request,id):
    
    profile=Profile.objects.get(id=id)
    current_user = request.user
    #profile=Profile.objects.filter(id=profile_id)
    ratings=Rating.objects.filter(profile_id=profile.id)
   
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            profile_rating = form.save(commit=False)
            # project_rating.average_vote=round((project_rating.usability + project_rating.content+ project_rating.design)/3)
            # project_rating.project=project
            project_rating.user=current_user
            profile_rating.save()
            return redirect('profile')
    else: 
        form=RateForm()
    
    return render(request, 'rating.html', {'form':form, 'profile':profile})

def rate_officer(request,profile_id):
   
    profiles=Profile.objects.filter(id=profile_id)
    ratings=Rating.objects.filter(profile_id=profiles)
    average_rating=[]
    mean_rate=0 
        
    for rate in ratings:
        average_rating.append(rate.rating)
            
    total_rates=sum(average_rating)
    if len(ratings)>0:
        total_rating=total_rates/len(ratings)
        mean_rate=total_rating
    else:
        total_rating=0
        mean_rate=total_rating  
    
    return render(request, 'profile.html',{'profiles':profiles,'mean_rate':mean_rate})
