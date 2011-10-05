# ============================================================ IMPORTS ==

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


# ============================================================ INIT ==

admin.autodiscover()


# ============================================================ PATTERNS ==

urlpatterns = patterns('ten-rock-solid-layouts',
  
  url(r'^', include('website.urls')),
  #url(r'^$', 'website.views.index', name='base'),
  #url(r'^template/three-boxes/$', 'website.views.template_threeboxes', name='template_threeboxes'),
  
  url(r'^admin/', include(admin.site.urls)),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('',
    url(r'^_assets/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, 
        'show_indexes': True, }
    )
)

