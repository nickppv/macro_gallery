from django.contrib import admin
from .models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ordering = ['title', ]
    search_fields = ['title', 'description']
    list_display = ['title', 'description', 'tag_list', 'created_at', 'published_date', 'photo']
    list_editable = ['description',]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
