from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('timeoff/create', views.create, name='create'),
    path('timeoff/<int:id>/delete', views.destroy, name='destroy'),
    path('', views.index, name='index'),
]
