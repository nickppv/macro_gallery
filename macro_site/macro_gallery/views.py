from django.shortcuts import render
import json
from .models import Photo


def index(request):
    all_photo = Photo.objects.all()
    # создаем список путей для картинок верхней галереи
    all_photo_small = Photo.objects.all().values_list('photo', flat=True)
    path_to_picture = ['/media/' + i for i in all_photo_small]

    return render(request,
                  'macro_gallery/index.html',
                  {'all_photo': all_photo,
                   'images_top_gallery': json.dumps(path_to_picture), })
