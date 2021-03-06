from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from users.api.process import *


urlpatterns = patterns('',
    url(r'^api/v1/createuser',create_user),
    url(r'^api/v1/showusers',show_users),
    url(r'^api/v1/userdetails/(\d+)/$',user_details),
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^myproj/', include('myproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
