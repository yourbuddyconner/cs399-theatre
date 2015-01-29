from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.settings import MEDIA_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^directions', 'app.views.directions', name='directions'),
    url(r'^merchandise', 'app.views.merchandise', name='merchandise'),
    url(r'^tickets', 'app.views.tickets', name='tickets'),
    url(r'^shows', 'app.views.shows', name='shows'),
    url(r'^admin/', include(admin.site.urls)),
    # For serving media files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),

    # url(r'^admin/', include(admin.site.urls)),
)
