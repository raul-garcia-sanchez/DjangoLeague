from django.urls import path

from . import views

app_name = 'league'
urlpatterns = [
    path('', views.clasificacion, name='clasificacion'),
]