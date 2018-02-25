from django.shortcuts import render
from . import models
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    model = models.IndexModel
    template_name = 'index.html'
    context_object_name = 'image_list'


class WorkListView(generic.ListView):
    model = models.WorkModel
    template_name = 'work_list.html'
    context_object_name = 'work_list'

class BathListView(generic.ListView):
    model = models.WorkModel
    template_name = 'bath_list.html'
    context_object_name = 'work_list'

class CousinesListView(generic.ListView):
    model = models.WorkModel
    template_name = 'cousines_list.html'
    context_object_name = 'work_list'

class FireplaceListView(generic.ListView):
    model = models.WorkModel
    template_name = 'fireplaces_list.html'
    context_object_name = 'work_list'

class FloorListView(generic.ListView):
    model = models.WorkModel
    template_name = 'floor_list.html'
    context_object_name = 'work_list'

class OutListView(generic.ListView):
    model = models.WorkModel
    template_name = 'out_list.html'
    context_object_name = 'work_list'

class FireplaceListView(generic.ListView):
    model = models.WorkModel
    template_name = 'fireplaces_list.html'
    context_object_name = 'work_list'

class StairsListView(generic.ListView):
    model = models.WorkModel
    template_name = 'stairs_list.html'
    context_object_name = 'work_list'

class ArtListView(generic.ListView):
    model = models.WorkModel
    template_name = 'art_list.html'
    context_object_name = 'work_list'

class MarbleListView(generic.ListView):
    model = models.WorkModel
    template_name = 'marble_list.html'
    context_object_name = 'work_list'

class GraniteListView(generic.ListView):
    model = models.WorkModel
    template_name = 'granite_list.html'
    context_object_name = 'work_list'

class QuartzListView(generic.ListView):
    model = models.WorkModel
    template_name = 'quartz_list.html'
    context_object_name = 'work_list'

class SingleView(generic.DetailView):
    model = models.WorkModel
    template_name = 'work_single.html'
    context_object_name = 'details_view'
