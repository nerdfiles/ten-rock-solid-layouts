# ============================================================ IMPORTS ==

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# ============================================================ INIT ==

admin.autodiscover()


# ============================================================ PATTERNS ==

urlpatterns = patterns('ten_rock_solid_layouts',
  url(r'^$', include('website.urls')),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^_assets/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, 
        'show_indexes': True, }
    )
)

