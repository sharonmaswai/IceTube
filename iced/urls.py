from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static



urlpatterns=[
	url(r'^$',views.usersignup,name='register'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),  
    url(r'^home/', views.home,name='home'),
    url(r'^newprofile/', views.create_profile, name='profile-form'),
    url(r'^profile/(\d+)/', views.profile, name='profile'),
    #url(r'^rate_project', views.rate_project, name='rate_project'),
    url(r'^rate_form/(\d+)/',views.rate, name='rateform'),
    # url('^$',views.dummy,name='dumm'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


