from django.contrib import admin
from .models import Instructor

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'website', 'specialisation')
    search_fields = ('user', 'specialisation')

admin.site.register(Instructor, InstructorAdmin)