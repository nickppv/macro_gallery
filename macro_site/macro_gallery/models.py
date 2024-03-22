from django.db import models

from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField


class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")
    information = models.TextField(blank=True, verbose_name="Интересная информация")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата создания")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    photo = ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Изображение")
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фоточки'
