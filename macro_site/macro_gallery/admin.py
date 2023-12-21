from django.contrib import admin
from .models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ordering = ['title', ]
    search_fields = ['title', 'description']
    list_display = ['title', 'description', 'created_at', 'published_date', 'photo']
