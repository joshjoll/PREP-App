from django.contrib import admin

from .models import Project, Review, Project, Image

# Register your models here.


admin.site.register(Review)
admin.site.register(Project)
admin.site.register(Image)
