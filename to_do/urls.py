from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name= 'landing'),
    path('singup/',views.singup, name= 'singup'),
    path('sigin/',views.sigin, name= 'sigin'),
    path("home/", views.home , name="home"),
    path("logout/",views.close_sesion, name= 'logout'),
    #CRUD Project
    path("projects/", views.project, name= 'project'),
    path("create_projects/", views.create_project, name= 'create_project'),
    path("update_projects/{id}", views.update_project, name= 'update_project'),
    path("delete_projects/<int:id>", views.delete_project, name= 'delete_project'),
    path("detail_project/<int:id>", views.detail_project, name= 'detail_project'),

    #CRUD Task
    path("create_task/<int:id>", views.create_task, name= 'create_task')
]