from  django.urls import path
from . import views

urlpatterns = [
    path('',views.appelJson),
    path('historique/',views.Historique.as_view(), name='appel-historique'),
]