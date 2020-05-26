from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
from poyosei.ressources import PlanteurResource, mouvementResource
from tablib import Dataset
import json
# @csrf_exempt


def typeMouvementListe(request):
    typeMouv = typeMouvement.objects.all()
    return render(request, 'typeMouvement/liste.html', {'active_tab': 'typeMouvement', 'typeMouv': typeMouv} )


def AjouterTypeMouvement(request):
    #Revoir le nom de la methode
    form = TypeMouvementForm()
    
    if request.method == 'POST':
        form = TypeMouvementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('poyosei:mouvementListe')

    else:
        form = TypeMouvementForm()

    return render(request, 'typeMouvement/ajouter.html', {'form':form, })

def typeMouvementEditer(request, Nom_mouvement):
    #Revoir le nom de la methode
    instance = get_object_or_404(TypeMouvement, Nom_mouvement=Nom_mouvement)
    form = TypeMouvementForm(request.POST or None, instance=instance)

    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('poyosei:typeMouvementListe')
    else:
        form = TypeMouvementForm(request.POST or None, instance=instance)


    return render(request, 'typeMouvement/editer.html', {'form':form, 'active_tab':'typeMouvement', 'instance':instance})        


def typeMouvementFiche(request, Nom_mouvement):
    instance = get_object_or_404(TypeMouvement, Nom_mouvement=Nom_mouvement)
    form = TypeMouvementForm(request.POST or None, instance=instance)

    return render(request, 'typeMouvement/fiche.html', {'form':form, 'active_tab':'typeMouvement', 'instance':instance})


def typeMouvementSupprimer(request, Nom_mouvement):
    instance = get_object_or_404(TypeMouvement, Nom_mouvement=Nom_mouvement)
    instance.delete()

    return redirect('poyosei:typeMouvementListe')







        
        
