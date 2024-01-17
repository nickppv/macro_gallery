from django.contrib import admin
from .models import Photo
from django.forms import TextInput, Textarea
from django.db import models


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ordering = ['title', ]
    search_fields = ['title', 'description']
    list_display = ['title', 'description', 'tag_list', 'information', 'published_date', 'photo']
    list_editable = ['description', 'information']

    # для изменения размера поля в админке, сделал меньше TextField
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '30'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())



