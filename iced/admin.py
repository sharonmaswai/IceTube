# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile, Rating

from django.contrib import admin
from .models import Profile, Rating

# Register your models here.
admin.site.register(Profile)
admin.site.register(Rating)
