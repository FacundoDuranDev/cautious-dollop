from django.urls import path
from .views import Agregar, Eliminar, Listar

urlpatterns = [
    path(
        'agregar/<str:nombre>',
        Agregar.as_view(),
        name='agregar'
    ),
    path(
        'eliminar/<str:nombre>',
        Eliminar.as_view(),
        name='eliminar'
        ),
    path(
        'listar',
        Listar.as_view(),
        name='listar'
    ),
]
