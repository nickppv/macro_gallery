from django.apps import AppConfig


class MacroGalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'macro_gallery'
    verbose_name = "Галерея макрофотографий"  # изменили имя приложения в админке на русское
