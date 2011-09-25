# ============================================================ IMPORTS ==

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# ============================================================ INIT ==

admin.autodiscover()


# ============================================================ PATTERNS ==

urlpatterns = patterns('ten_rock_solid_layouts',
  url(r'^$', include('website.urls')),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
# + staticfiles_urlpatterns()


