from __future__ import absolute_import

from crowdsourcing.views import (allowed_actions,
                    embeded_survey_questions,
                    embeded_survey_report,
                    location_question_results,
                    location_question_map,
                    questions,
                    submissions,
                    submission,
                    submission_for_map,
                    survey_detail,
                    survey_report)
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crtcp.views.home', name='home'),
    # url(r'^crtcp/', include('crtcp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userena.urls')),
    ('^$', redirect_to, {'url':'/home/' }),
    url(r'^survey/submissions/$',
        submissions,
        {"format": "json"},
        name='submissions'),

    url(r'^survey/submissions/(?P<format>[a-z]+)/$',
        submissions,
        name='submissions_by_format'),

    url(r'^survey/submission/(?P<id>\d+)/$',
        submission),

    url(r'^survey/submission_for_map/(?P<id>\d+)/$',
        submission_for_map),

    url(r'^survey/location_question_results/(?P<question_id>\d+)/(?P<limit_map_answers>\d+)/$',
        location_question_results,
        kwargs={"survey_report_slug": ""}),

    url(r'^survey/location_question_results/(?P<question_id>\d+)/(?P<limit_map_answers>\d*)/(?P<survey_report_slug>[-a-z0-9_]*)/$',
        location_question_results,
        name="location_question_results"),

    url(r'^survey/location_question_map/(?P<question_id>\d+)/(?P<display_id>\d+)/$',
        location_question_map,
        name="location_question_map"),

    url(r'^survey/location_question_map/(?P<question_id>\d+)/(?P<display_id>\d+)/(?P<survey_report_slug>[-a-z0-9_]*)/$',
        location_question_map,
        name="location_question_map"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/$',
        survey_detail,
        name="survey_detail"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/api/allowed_actions/$',
        allowed_actions,
        name="allowed_actions"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/api/questions/$',
        questions,
        name="questions"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/api/embeded_survey_questions/$',
        embeded_survey_questions,
        name="embeded_survey_questions"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/api/report/$',
        embeded_survey_report,
        {"report": ""},
        name="embeded_survey_report_default"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/api/report/(?P<report>[-a-z0-9_]+)/$',
        embeded_survey_report,
        name="embeded_survey_report"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/report/$',
        survey_report,
        name="survey_default_report_page_1"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/report/(?P<page>\d+)/$',
        survey_report,
        name="survey_default_report"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/(?P<report>[-a-z0-9_]+)/$',
        survey_report,
        name="survey_report_page_1"),

    url(r'^survey/(?P<slug>[-a-z0-9_]+)/(?P<report>[-a-z0-9_]+)/(?P<page>\d+)/$',
        survey_report,
        name="survey_report"),

    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT})
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
