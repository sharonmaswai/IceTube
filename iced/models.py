# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(default='image.png',upload_to='profiles/')
    name=models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    bio = HTMLField(max_length=500,default='About me')
    task= IntergerField()

    def save_profile(self):
        self.save()
        

    def __str__(self):
        return self.bio