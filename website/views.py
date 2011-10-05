# ============================================================ IMPORTS

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template


# ============================================================ VIEWS UTILS

"""

FUNCTION
NAME: render_response
USAGE: render_response(request, 'foo_base.html', {'foo': Foo.objects.all()})

"""

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


# ============================================================ VIEWS FUNCTIONS    
        
def template_base(self):
    #return render_to_response('website/base.html', {}, context_instance=RequestContext(request))

    return direct_to_template(self, 'website/template-base.html', {
        'extra-context': '',
    })
    
def template_threeboxes(self):

    return direct_to_template(self, 'website/template-threeboxes.html', {
        'extra-context': '',
    })
