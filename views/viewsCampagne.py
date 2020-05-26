from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
#from poyosei.ressources import campagneResource, mouvementResource
from tablib import Dataset
import json
# @csrf_exempt




def campagne(request):
    return render(request, 'campagne/index.html', {"active_tab": "campagne"})

def campagneListe(request):
    campagne = Campagne.objects.all()

    return render(request, 'campagne/liste.html', {'active_tab': 'campagne', 'campagne': campagne})

def campagneAjouter(request):
    campagnes = Campagne.objects.all()
    if request.method == 'POST':
        form = CampagneForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('poyosei:campagneListe')
    else:
        form = CampagneForm()
    
    return render(request, 'campagne/ajouter.html', {'active_tab': 'campagne', 'active_tabP': 'ajout', 'form': form, 'campagnes': campagnes})

def campagneEditer(request, pacage, annee):
    campagnes = Campagne.objects.all()
    instance = get_object_or_404(Campagne, pacage=pacage, annee=annee)
    form = CampagneForm(request.POST or None, instance=instance)
 
    if form.is_valid():
        form.save(commit=False)
        form.save()

    return render(request, 'campagne/editer.html', {'form': form,  'active_tab': 'campagne', 'campagnes': campagnes, 'instance': instance})

def campagneSupprimer(request, pacage, annee, id):
    campagnes = Campagne.objects.all()
    query = get_object_or_404(Campagne, pacage=pacage)
    query.delete()

    return redirect('poyosei:campagneListe')


def campagneFiche(request, pacage, annee):
    campagnes = Campagne.objects.all()
    instance = get_object_or_404(Campagne, pacage=pacage, annee=annee)
    form = CampagneForm(request.POST or None, instance=instance)

    if form.is_valid():
        campagne = form.save(commit=False)
        campagne.save()

    return render(request, 'campagne/fiche.html', {'form': form, 'active_tab': 'campagne', 'campagnes': campagnes, 'instance': instance})