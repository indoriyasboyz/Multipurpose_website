from django.views import generic
from .models import Why_choose_us, Team
# Create your views here.


"""def about(request):
    choose = Why_choose_us.objects.all()
    teams = Team.objects.all()
    return render(request, 'about/about.html', {'choose': choose, 'teams': teams})"""


class Aboutview(generic.ListView):
    template_name = 'about/about.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Why_choose_us.objects.all()

    def get_context_data(self, **kwargs):
        about = super(Aboutview, self).get_context_data(**kwargs)
        about['choose'] = Why_choose_us.objects.all()
        about['teams'] = Team.objects.all()

        return about


