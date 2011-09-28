from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('CommandJob.views',
    (r'^$', 'index'),
    (r'^(?P<job_id>\d+)/status$', 'status'),    
    (r'^(?P<job_id>\d+)/kill$', 'kill'),
    (r'^add/(?P<cmdline>.*$)', 'add')
)


