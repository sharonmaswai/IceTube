# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 
from django.core.validators import MaxValueValidator

from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(default='image.png',upload_to='profiles/')
    name=models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    bio = HTMLField(max_length=500,default='About me')
    task= models.IntegerField()
    county=models.CharField(max_length=50,default='Kajiado')
    specialisation=models.CharField(max_length=50,default='Livestock')

    def save_profile(self):
        self.save()
        

    def __str__(self):
        return self.name
class Rating(models.Model):
   
    rating = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    officer = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    average_vote=models.FloatField(default=0)
 
    
    def save_rating(self):
       
        self.save()
        
    def delete_rating(self):
        
        self.delete()
        
    def update_rating(self):
       
        self.update()
        
   
    def __str__(self):
        return self.name        

class  KonnectDetails(models.Model):
    name=models.CharField(max_length=30)
    county=models.CharField(max_length=50,default='Kajiado')
    specialisation=models.CharField(max_length=50,default='Livestock')