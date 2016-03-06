from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader

# from django.core.urlresolvers import reverse
# from django.views.generic import TemplateView
# from django.views import generic
# from django.utils import timezone
# from PIL import Image

from .models import Tour, TourImage

def toursList(request):
    tours = Tour.objects.all()
    template = loader.get_template('tours/tours-list.html')
    
    context = {}
    context['tours'] = []
    for tour in tours:
        context['tours'].append((tour,tour.getMainImage()))

    return HttpResponse(template.render(context, request))

def toursDetail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    tourImgs = TourImage.objects.filter(tour_id=tour_id, visible=True)
    
    context = {
        'tour': tour,
    }
    context['imgs'] = []
    for tourImg in tourImgs:
        context['imgs'].append(tourImg.image)

    template = loader.get_template('tours/tour-details.html')

    return HttpResponse(template.render(context, request))
