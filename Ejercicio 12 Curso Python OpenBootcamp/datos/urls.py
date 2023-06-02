from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path('directores/', views.directores, name='directores'),
    re_path('peliculas/', views.peliculas, name='peliculas')
]