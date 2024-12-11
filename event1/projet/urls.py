from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('creer_evenement/', views.creer_evenement, name='creer_evenement'),
    path('connexion.html', views.connexion, name='connexion'),
    path('inscription.html', views.inscription, name='inscription'),
     path('event_list', views.event_list, name='event_list'),
]