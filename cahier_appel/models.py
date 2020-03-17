from django.db import models
import os
from identite.models import Eleve, Professeur

# Create your models here.

class Appel(models.Model):
    cour = models.CharField(max_length=60)
    absent = models.ManyToManyField(Eleve)
    horodage = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cour} du {self.horodage}"
