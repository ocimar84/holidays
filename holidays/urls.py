from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    path("timeoffs/create", views.create, name="create"),
    path("timeoffs", views.show, name="show"),
    path("", views.index, name="index"),
]
