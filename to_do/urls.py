from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name= 'landing'),
    path('singup/',views.singup, name= 'singup'),
    path('sigin/',views.sigin, name= 'sigin'),
    path("home/", views.home , name="home"),
    path("logout/",views.close_sesion, name= 'logout')
]
