from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Blogs

# Create your views here.


class Blogview(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Blogs.objects.all()

    def get_context_data(self, **kwargs):
        blog = super(Blogview, self).get_context_data(**kwargs)
        blog['blogs'] = Blogs.objects.all()

        return blog
