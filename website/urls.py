# ============================================================ IMPORTS

from django.conf.urls.defaults import *


# ============================================================ PATTERNS

urlpatterns = patterns('website.views',
  url(r'^$', 'template_base', name='template_base'),
  url(r'^template/three-boxes/$', 'template_threeboxes', name='template_threeboxes'),
  url(r'^template/3d-screenshots/$', 'template_3dscreenshots', name='template_3dscreenshots'),
)
