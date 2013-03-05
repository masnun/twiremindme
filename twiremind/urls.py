from django.conf.urls import patterns, include, url
from twiremind.settings import DEBUG, STATIC_ROOT, MEDIA_ROOT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from twiremind.core.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twiremind.views.home', name='home'),

    #Auth
    url(r'^register$', register, name='register'),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),


    # Logged In users
    url(r'^$', front, name='front'),
    url(r'^home$', home, name='home'),
    url(r'^delete$', delete, name='delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



