from django.urls import path
from . import views

app_name = 'macro_gallery'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<slug:tag_slug>/', views.index, name='result_by_tag'),
    path('search/', views.search, name='search'),
]
