from django.conf.locale import et
from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Slider, Services, News

# Create your views here.


"""def home(request):
    sliders = Slider.objects.all()
    services = Services.objects.all()
    return render(request, 'home/index.html', {'sliders': sliders, 'services': services})"""


class Homeview(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Slider.objects.all()

    def get_context_data(self, **kwargs):
        home = super(Homeview, self).get_context_data(**kwargs)
        home['sliders'] = Slider.objects.all()
        home['services'] = Services.objects.all()
        home['details'] = News.objects.all()

        return home

