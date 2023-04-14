from django.contrib import admin
from django.urls import include, path

from laLliga import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('laLliga/',include('laLliga.urls'))
]