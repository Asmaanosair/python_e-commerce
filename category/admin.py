from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin) :
    list_filter=('active','name')
    list_display=('active','name','slug')

admin.site.register(Category,CategoryAdmin)