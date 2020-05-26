from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
#from poyosei.ressources import PlanteurResource, mouvementResource
from django.views.generic import ListView



class PlanteurListView(ListView):
    model = Planteur
    def get_queryset(self):
        history = Planteur.history.all()
        
        return history
