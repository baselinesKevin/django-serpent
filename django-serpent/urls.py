from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^mysite/', include('mysite.foo.urls')),

    (r'^$', 'django-serpent.serpent.views.index'),
    (r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^serpent/$', 'django-serpent.serpent.views.index'),
    (r'^serpent/(?P<module_id>[0-9a-f]{8})/$', 'django-serpent.serpent.views.createRPEJob'),
    (r'^serpent/download/$', 'django-serpent.serpent.views.download'),
    (r'^serpent/download/(?P<filename>.*)$', 'django-serpent.serpent.views.download')

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
