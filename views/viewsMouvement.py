from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
from poyosei.ressources import PlanteurResource, mouvementResource
from tablib import Dataset
import json
# @csrf_exempt



def mouvementListe(request):
    mouvements = Mouvement.objects.all().filter(année_concerne__gte=Campagne.CampagneEnCours())
    #active_tab = 'mouvement'

    return render(request, 'mouvement/liste.html', {'active_tab': 'mouvement', 'mouvements': mouvements})


def mouvementAjouter(request):
    mouvements = Mouvement.objects.all()
    mouv = typeMouvement.objects.get(Nom_mouvement='Transfert de référence individuelle sans foncier')
    phrase = mouv.Nom_mouvement
    form = MouvementForm()
    if request.method == 'POST':
        form = MouvementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('poyosei:mouvementListe')

    else:
        form = MouvementForm()



    return render(request, 'mouvement/ajouter.html', {'form': form, 'active_tab': 'mouvement', 'active_tabM': 'ajout', 'phrase':phrase, 'mouvements': mouvements})


def mouvementEditer(request, pacage_cedant, pacage_repreneur, id):
    mouvements = Mouvement.objects.all()
    instance = get_object_or_404(Mouvement, pacage_cedant=pacage_cedant, pacage_repreneur=pacage_repreneur, id=id)
    form = MouvementForm(request.POST or None, instance=instance)

    if form.is_valid():
        mouvement = form.save(commit=False)
        mouvement.save()

    return render(request, 'mouvement/editer.html', {'mouvements':mouvements, 'form':form, 'instance':instance })

def mouvementSupprimer(request, pacage_cedant, pacage_repreneur, id):
    mouvements = Mouvement.objects.all()
    query = get_object_or_404(Mouvement, pacage_cedant=pacage_cedant, pacage_repreneur=pacage_repreneur, id=id)
    query.delete()

    return redirect('poyosei:mouvementListe')

def mouvementFiche(request, pacage_cedant, pacage_repreneur, id):
    mouvements = Mouvement.objects.all()
    instance = get_object_or_404(Mouvement, pacage_cedant=pacage_cedant, pacage_repreneur=pacage_repreneur, id=id)
    form = MouvementForm(instance=instance)

    if form.is_valid():
        mouvement = form.save(commit=False)
        mouvement.save()

    return render(request, 'mouvement/fiche.html', {'form':form, 'mouvements':mouvements, 'instance':instance})

def mouvementHistorique(request):
    historique = Mouvement.history.all()

    return render (request, 'mouvement/historique.html', {'historique':historique} )



        