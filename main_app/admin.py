from django.contrib import admin
from .models import Project, Review, Image, Technology, User_Details

# Register your models here.


admin.site.register(Review)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Technology)
admin.site.register(User_Details)
