from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('serpent.views',
    (r'^$', 'index'),
    (r'^(?P<module_id>[0-9a-f]{8})/$', 'createRPEJob'),
    (r'^download/$', 'download'),
    (r'^download/(?P<filename>.*)$', 'download')
)
