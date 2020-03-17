from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'guid']

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'matiere', 'guid']

@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    pass

@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    pass

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    pass