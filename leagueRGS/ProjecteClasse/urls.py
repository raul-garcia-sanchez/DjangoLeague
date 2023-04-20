from django.contrib import admin
from django.urls import include, path

from laLliga import views
from laLliga.views import *
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laLliga/',include('laLliga.urls')),
    path("password_change/", PasswordChangeView.as_view(template_name="leagueRGS/laLliga/templates/registration/change_password.html"),
         name='change_password'),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", profile, name="profile"),
    
   
]