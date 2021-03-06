from django.conf.urls import url, include
from . import views

test_patterns = [
	url(r'^$', views.index, name='payments_index'),
	url(r'^oauth/success', views.oauth_success, name='test_oauth_success'),
	url(r'^stk-push/success', views.stk_push_success, name='test_oauth_success'),
]

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^icedtube/', include(test_patterns)),
]