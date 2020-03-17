from django.db import models
from identite.models import *
from uuid import uuid1

# Create your models here.


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    valeur = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.eleve} a obtenu {self.valeur} en {self.matiere} le {self.date}"


class Matiere(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

