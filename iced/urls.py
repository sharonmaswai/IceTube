from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns=[
    
    
    url(r'^newprofile/', views.create_profile, name='profile-form'),
    url(r'^profile/$', views.profile, name='profile'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
