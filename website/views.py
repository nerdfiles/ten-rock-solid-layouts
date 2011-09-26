# ============================================================ IMPORTS

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
#from django.http import HttpResponse, Http404


# ============================================================ VIEWS FUNCTIONS

def index(request, context):
  #latest_OBJ_list = OBJ.objects.all().order_by('-pub_date')[:5]
  #return render_to_response('website/index.html', {'latest_OBJ_list': latest_OBJ_list})
  return render_to_response('website/base.html', context_instance=RequestContext(request, context))