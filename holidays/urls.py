from django.urls import path

from . import views

urlpatterns = [
    path("timeoffs/create", views.create, name="create"),
    path("timeoffs", views.show, name="show"),
    path("", views.index, name="index"),
]
