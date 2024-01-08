from django.db import models

from taggit.managers import TaggableManager


class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фоточки'
