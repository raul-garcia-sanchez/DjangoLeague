from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classificacio',views.classificacio),
    path('classificacio/<int:lliga_id>',views.classificacio, name="classificacio"),
    path('menu',views.menu),
    path('crearLliga',views.crearLliga, name="crearLliga"),
    path('crea_Partit',views.crearPartit, name="crearPartit"),
    path('crea_Partit/<int:lliga_id>',views.triarEquipsPartit, name="triarEquipsPartit"),
]