import django
if django.VERSION > 1.5:
    from django.conf.urls import patterns, include, url
else:
    from django.conf.urls.defaults import *

    
    
    
from .views import DajaxiceRequest

urlpatterns = patterns('dajaxice.views',
    url(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
    url(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
)

