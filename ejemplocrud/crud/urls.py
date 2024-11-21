from django.urls import path
from . import views

## Direccionamiento para servidor de imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('crud', views.cruds, name='crud'),
    path('crud/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('prueba', views.prueba, name='prueba'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)