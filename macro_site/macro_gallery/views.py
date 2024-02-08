from random import sample
from PIL import Image
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from .models import Photo
from taggit.models import Tag


def choose_picture_for_slider(i) -> list:
    '''
    выбираем изображения с пейзажной ориентацией
    '''
    image = Image.open(getattr(i, 'photo'))
    w, h = image.size
    if w > h:
        return image


def index(request, tag_slug=None):

    all_photo = Photo.objects.all()

    # выбираем элемент из queryset, проверяем его размер и добавляем в список
    # выбираем в слайдер пять случайных записей из списка
    slider_photo_list = []
    for i in all_photo:
        if choose_picture_for_slider(i):
            slider_photo_list.append(i)
    slider_photo_list = sample(slider_photo_list, 5)

    # создаем поиск по тегу
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_photo = all_photo.filter(tags__in=[tag])
    # случайная выборка изображений для слайдера
    results = all_photo.order_by('?')

    return render(request,
                  'macro_gallery/index.html',
                  {'title': 'Главная страница',
                   'results': results,
                   'slider_photo_list': slider_photo_list, })


def search(request):
    all_photo = Photo.objects.all()
    slider_photo_list = []
    for i in all_photo:
        if choose_picture_for_slider(i):
            slider_photo_list.append(i)
    slider_photo_list = sample(slider_photo_list, 5)

    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Photo.objects.annotate(
                search=SearchVector('title', 'description', 'tags__name'),
                ).filter(search=query).values('id').distinct()
            results = Photo.objects.filter(id__in=results).order_by('?')

    return render(request,
                  'macro_gallery/index.html',
                  {'title': f'Поиск по: {query}',
                   'form': form,
                   'query': query,
                   'results': results,
                   'slider_photo_list': slider_photo_list, })
