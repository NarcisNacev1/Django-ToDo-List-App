#define paths to different web pages
from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view")
]