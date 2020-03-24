from django.urls import path
from django.conf import settings
from .views import Blogview
urlpatterns = [
    path('blog', Blogview.as_view(), name='blogs'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    # from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)