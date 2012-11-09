from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from crtcp.api import UPAIResource

admin.autodiscover()

upaiResource = UPAIResource()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crtcp.views.home', name='home'),
    # url(r'^crtcp/', include('crtcp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(upaiResource.urls)),
    (r'^accounts/', include('userena.urls')),
    ('^$', redirect_to, {'url':'/home/' }),
    (r'^surveys/', include('crowdsourcing.urls')),
    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT})
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
