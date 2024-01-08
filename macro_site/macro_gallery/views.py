import json
from random import sample
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Photo
from taggit.models import Tag


def index(request, tag_slug=None):
    all_photo = Photo.objects.all()
    only_one = all_photo[0]

    # создаем поиск по тегу
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_photo = all_photo.filter(tags__in=[tag])
    # создаем список путей для картинок верхней галереи
    all_photo_small = Photo.objects.all().values_list('photo', flat=True)
    path_to_picture = ['/media/' + i for i in all_photo_small]
    # случайная выборка изображений для слайдера
    images_for_slider = sample(path_to_picture, 5)

    return render(request,
                  'macro_gallery/index.html',
                  {
                   'all_photo': all_photo,
                   'only_one': only_one,
                   'images_top_gallery': json.dumps(path_to_picture),
                   'images_for_slider': images_for_slider,
                  })

