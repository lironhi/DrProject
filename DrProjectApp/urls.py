from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login, name='login'),
    path('newanalyze', views.newanalyze, name='newanalyze'),
    path('home', views.home, name='home'),
    path('registration_new_patient', views.registration_new_patient),
    path('login_dr', views.login_dr),
    path('txtcreator', views.txtcreator),
    

]