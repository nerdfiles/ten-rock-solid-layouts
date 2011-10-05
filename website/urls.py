# ============================================================ IMPORTS

from django.conf.urls.defaults import *


# ============================================================ PATTERNS

urlpatterns = patterns('website.views',
  url(r'^$', 'index', name='base'),
  url(r'^template/three-boxes/$', 'template_threeboxes', name='template_threeboxes'),
)
