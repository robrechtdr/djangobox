from django.shortcuts import render_to_response
from django.template import RequestContext

def viewbox(request):
    name = "Rimururu"
    return render_to_response('viewbox.html', {'name': name},
      context_instance=RequestContext(request))

