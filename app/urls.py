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
	url(r'^giftcards', 'app.views.giftcards', name='giftcards'),
    url(r'^show1', 'app.views.show1', name='show1'),
    url(r'^show2', 'app.views.show2', name='show2'),
    url(r'^show3', 'app.views.show3', name='show3'),
    url(r'^show4', 'app.views.show4', name='show4'),
    url(r'^show5', 'app.views.show5', name='show5'),
    url(r'^admin/', include(admin.site.urls)),
    # For serving media files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),

    # url(r'^admin/', include(admin.site.urls)),
)
