from random import sample
from PIL import Image
from django.core.paginator import Paginator
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
    title = 'Главная страница'
    all_photo = Photo.objects.all()

    # выбираем элемент из queryset, проверяем его размер и добавляем в список
    # выбираем в слайдер пять случайных записей из списка
    slider_photo_list = []
    slider_random_choice = all_photo.order_by('?')
    for i in slider_random_choice:
        if choose_picture_for_slider(i):
            slider_photo_list.append(i)
    slider_photo_list = sample(slider_photo_list, 5)

    # создаем поиск по тегу
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_photo = all_photo.filter(tags__in=[tag])
        title = f'Результаты поиска по тегу: {tag}'
    results = all_photo

    paginator = Paginator(all_photo, 10)  # сколько изображений будет на странице
    page_number = request.GET.get('page')  # в переменную page_number передаем полученный номер страницы
    results = paginator.get_page(page_number)  # получаем все картинки для соответствующей страницы

    return render(request,
                  'macro_gallery/index.html',
                  {'title': title,
                   'results': results,
                   'slider_photo_list': slider_photo_list,
                   })


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
            results = Photo.objects.filter(id__in=results)

            paginator = Paginator(results, 5)
            page_number = request.GET.get('page')
            results = paginator.get_page(page_number)

    return render(
        request,
        'macro_gallery/index.html',
        {'title': f'Поиск по тегу: {query}' if query else 'Ничего не найдено',
         'form': form,
         'query': query,
         'results': results,
         'slider_photo_list': slider_photo_list, }
        )
