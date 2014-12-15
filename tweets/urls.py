from django.conf.urls.defaults import patterns, url
from schema.create import create_tables

urlpatterns = patterns('tweets.views',
    url(r'^/?$', 'timeline', name='timeline'),
    url(r'^public/$', 'publicline', name='publicline'),
    url(r'^(?P<username>\w+)/$', 'userline', name='userline'),
)

create_tables()
