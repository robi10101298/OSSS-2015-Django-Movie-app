from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'myapp.views.landing_page'),

    # Admin URL's
    url(r'^admin/$', 'myapp.views.adminpanel'),
    url(r'^admin/settings/', include(admin.site.urls)),
    url(r'^scrape/$', 'myapp.views.video_scraping'),
    url(r'^logout/$', 'myapp.views.logout_user'),
)
