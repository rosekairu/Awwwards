from django.contrib import admin
from .models import Profile, Project, Rate, Comment


# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rate)
admin.site.register(Comment)


