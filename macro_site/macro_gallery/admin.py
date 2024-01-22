from django.contrib import admin
from django.utils.html import format_html
from django.forms import TextInput, Textarea
from django.db import models
from .models import Photo

from sorl.thumbnail.admin import AdminImageMixin
# from sorl.thumbnail import get_thumbnail


@admin.register(Photo)
class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):  # для миниаютюр сюда я добавил "AdminImageMixin"
    ordering = ['title', ]
    search_fields = ['title', 'description']
    list_editable = ['description', 'information']
    list_display = ['title', 'description', 'tag_list', 'information', 'published_date', 'image_tag',]

    # для изменения размера поля в админке, сделал меньше TextField
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '30'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def image_tag(self, obj):
        return format_html('<img src="{}" width="15%" height="15%"/>'.format(obj.photo.url))


