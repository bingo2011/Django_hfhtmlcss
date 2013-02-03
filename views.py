# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.http import Http404

def index(request):
    return render_to_response('starbuzz/index.html')

def staticpage(request, template):
    try:
        return direct_to_template(request, template)
    except TemplateDoesNotExist:
        raise Http404
