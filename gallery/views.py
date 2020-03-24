from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Gallery

# Create your views here.


class Galleryview(generic.ListView):
    template_name = 'gallery/gallery.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Gallery.objects.all()

    def get_context_data(self, **kwargs):
        home = super(Galleryview, self).get_context_data(**kwargs)
        home['gallery'] = Gallery.objects.all()

        return home
