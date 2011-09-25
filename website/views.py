# ============================================================ IMPORTS
from django.shortcuts import render_to_response
from django.http import HttpResponse


# ============================================================ VIEWS FUNCTIONS

def index(request):
  #latest_OBJ_list = OBJ.objects.all().order_by('-pub_date')[:5]
  #return render_to_response('website/index.html', {'latest_OBJ_list': latest_OBJ_list})
  return render_to_response('website/base.html',)