from django.contrib import admin
from .models import Section
# Register your models here.

class SectionAdmin(admin.ModelAdmin) :
    list_filter=('active','name')
    list_display=('active','name','slug')

admin.site.register(Section,SectionAdmin)
