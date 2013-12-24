#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tvapp import settings

admin.autodiscover()

urlpatterns = patterns('tvapp.whatsontv.views',
    (r'mor','more'),
    (r'^$','index'),
	(r'program/id=(?P<id>\w+)','detail'),
	(r'channel/id=tve','chlist1'),
	(r'channel/id=tve2','chlist2'),
	(r'channel/id=clan','chlistclan'),
	(r'channel/id=antena3','chlist3'),
	(r'channel/id=neox','chlistneox'),
	(r'channel/id=nova','chlistnova'),
	(r'channel/id=cuatro','chlist4'),
	(r'channel/id=telecinco','chlist5'),
	(r'channel/id=boing','chlistboing'),
	(r'channel/id=lasexta','chlist6'),
	(r'channel/id=lasexta3','chlist63')
) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()