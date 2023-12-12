"""
URL configuration for macro_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# настройки для отображения в админке вместо слов "Администрирование" и др.
admin.site.site_header = 'МакроЭтоЗбс!'
admin.site.index_title = 'Не устану повторять! Вы - прекрасный администратор'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('macro_gallery.urls', namespace='macro_gallery')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
