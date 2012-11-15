from django.conf.urls.defaults import *

urlpatterns = patterns('upais.views',
    (r'^$', 'upai_list'),
    (r'^id/(?P<upai_id>\d+)$', 'upai_card'),
#    (r'^something/$', 'something_view'),
)
