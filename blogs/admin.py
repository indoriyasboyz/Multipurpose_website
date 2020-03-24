from django.contrib import admin
from .models import Blogs, Blogtags
# Register your models here.

admin.site.register(Blogtags)
admin.site.register(Blogs)
