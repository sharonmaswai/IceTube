# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import Profile, Rating, KonnectProfile
from .forms import ProfileForm, RateForm,UserSignUpForm
from rest_framework.response import Response 
from rest_framework.views import APIView
from .serializer import KonnectSerializer



# Create your views here.
def welcome(request):
    return render(request, 'home/index.html')

    
@login_required(login_url='/accounts/login/')
def home(request):
	return render(request, 'home/home.html')
@login_required(login_url='/accounts/login/')
def bot(request):
	return render(request, 'bot.html')    


def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:
        form = UserSignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')


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
    
def profile(request, officer_id):
    current_user = request.user
   
    profiles=Profile.objects.filter(id=officer_id)
    # ratings=Rating.objects.filter(officer_id=profiles)
    # average_rating=[]
    # mean_rate=0 
        
    # for rate in ratings:
    #     average_rating.append(rate.rating)
            
    # total_rates=sum(average_rating)
    # if len(ratings)>0:
    #     total_rating=total_rates/len(ratings)
    #     mean_rate=total_rating
    # else:
    #     total_rating=0
    #     mean_rate=total_rating  
    
    
    return render(request,'profile/profile-view.html',{'profiles': profiles })
def rate(request,id):
    
    profile=Profile.objects.get(id=id)
    current_user = request.user
    #profile=Profile.objects.filter(id=profile_id)
    ratings=Rating.objects.filter(officer_id=profile.id)
   
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            profile_rating = form.save(commit=False)
            # project_rating.average_vote=round((project_rating.usability + project_rating.content+ project_rating.design)/3)
            # project_rating.project=project
            # profile_rating.user=current_user
            profile_rating.save()
            return redirect('profile', profile.id)
    else: 
        form=RateForm()
    
    return render(request, 'rating/rating.html', {'form':form, 'profile':profile})

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


class KonnectList(APIView):
    def get(self, request, format=None):
        all_details=KonnectProfile.objects.all()
        serializers=KonnectSerializer(all_details, many=True)

        return Response(serializers.data)
