from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic.list import ListView
from .models import *

# Create your views here.
def appelJson(req):
    data = serialize("json",Appel.objects.all())
    return JsonResponse(data,safe=False)

class Historique(ListView):
    model = Appel
    template_name = 'cahier_appel/historique.html'
    custom_context = {}

    def get(self, request, *args, **kwargs):
        print('iin get')
        self.custom_context.clear()
        if request.GET.__len__() >= 2:
            print('ok il est la')
            if request.GET['matiere'] != '':
                print('dans get')
                self.custom_context['matiere'] = request.GET['matiere']
                self.queryset = Appel.objects.filter(cour = request.GET['matiere'])
        return super().get(request,*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p'] = self.custom_context
        return context
