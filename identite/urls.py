from django.urls import path
from . import views

urlpatterns = [
    path('eleves/get/', views.listEleve, name='get-eleve'),
    path('professeurs/get/', views.listProffesseur, name='get-professeur'),
]