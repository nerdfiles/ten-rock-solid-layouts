# ============================================================ IMPORTS

from django.conf.urls.defaults import *
from django.contrib import admin


# ============================================================ PATTERNS

urlpatterns = patterns('website.views',
  url(r'^$', 'index', name='index'),
)

"""
  # generic views examples  
  (r'^$',
      ListView.as_view(
          queryset=OBJ.objects.order_by('-pub_date')[:5],
          context_object_name='latest_OBJ_list',
          template_name='website/index.html')),
  (r'^(?P<pk>\d+)/$', # item name name, eh
      DetailView.as_view(
          model=OBJ,
          template_name='website/page.html')), # reasonable item to choice
"""