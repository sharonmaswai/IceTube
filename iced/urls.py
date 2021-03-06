from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static



urlpatterns=[

   url(r'^$', views.welcome,name='welcome'),
   url(r'^home/', views.home,name='home'),
   url(r'^profile/', views.view_profile,name='profile'),
   url(r'^newprofile/', views.create_profile, name='profile-form'),
   #url(r'^profile/(\d+)/', views.profile, name='profile'),
   url(r'^rate_form/(\d+)/',views.rate, name='rateform'),
   url(r'^api/details/$',views.KonnectList.as_view()),
   url(r'^ibot/', views.bot,name='bot'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
