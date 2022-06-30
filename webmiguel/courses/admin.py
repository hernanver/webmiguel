from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Course, CourseAdmin)


# Register your models here.
