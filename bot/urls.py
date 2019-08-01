from django.contrib import admin
from django.conf.urls import url

from bot.views import home, get_response
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^get-response/$', views.get_response,name="response"),
]

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)