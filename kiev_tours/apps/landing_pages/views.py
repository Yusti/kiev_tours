from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader

# from django.core.urlresolvers import reverse
# from django.views.generic import TemplateView
# from django.views import generic
# from django.utils import timezone
# from PIL import Image

from .models import Tour

def home(request):
    tours = Tour.objects.all()
    template = loader.get_template('landing_pages/home.html')
    # context = {'aa' : "bb"}
    context = {
        'tours': tours,
    }
    return HttpResponse(template.render(context, request))
