from django.shortcuts import render_to_response
from django.template import RequestContext

def viewbox(request):
    name = "{{ project_name }}"
    return render_to_response('viewbox.html', {'name': name},
      context_instance=RequestContext(request))
