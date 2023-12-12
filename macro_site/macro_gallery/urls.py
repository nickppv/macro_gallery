from django.urls import path
from . import views

app_name = 'macro_gallery'

urlpatterns = [
    path('', path(views.index), name='index')
]