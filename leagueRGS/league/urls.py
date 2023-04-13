from django.urls import path

from . import views

app_name = 'league'
urlpatterns = [
    path('clasificacion/<int:liga_id>/', views.clasificacion, name='clasificacion'),
    path('pichichis/', views.pichichis, name='pichichis'),
    path('partidos/<int:partido_id>/', views.seguimiento_partido, name='seguimiento_partido'),
    path('menu/', views.menu, name='menu')
]