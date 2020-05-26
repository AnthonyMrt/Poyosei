# from django.views.decorators.csrf import csrf_exempt
# from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
# from django.views import View
from poyosei.forms import *
from poyosei.models import *
# from poyosei.ressources import PlanteurResource, mouvementResource
# from tablib import Dataset
# import json



def statsListe(request):
    statistiques =  Statistique.objects.all()
    return render(request, 'statistique/liste.html', {'active_tab': 'statistique', 'statistiques':statistiques})

def statsAjouter(request):
    statistiques = Statistique.objects.all()
    form =  StatistiqueForm()

    if request.method == 'POST':
        form = StatistiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poyosei:statsListe')
    else:
        form = StatistiqueForm()

    return render(request, 'statistique/ajouter.html', {'form':form, 'active_tab':'statistique', 'active_tabM': 'ajout', 'statistiques':statistiques })

def statsEditer(request, pacage, annee):
    statistiques = Statistique.objects.all()
    instance = get_object_or_404(Statistique, pacage=pacage, annee=annee)
    form = StatistiqueForm(request.POST or None, instance=instance)

    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('poyosei:statsListe')
    else:
        form = StatistiqueForm(request.POST or None, instance=instance)

    return render(request, 'statistique/editer.html', {'statistiques':statistiques, 'instance':instance, 'form':form })

def statsFiche(request, pacage, annee):
    statistiques = Statistique.objects.all()
    instance = get_object_or_404(Statistique, pacage=pacage, annee=annee)
    form = StatistiqueForm(request.POST or None, instance=instance)

    return render(request, 'statistique/fiche.html', {'statistiques':statistiques, 'instance':instance, 'form':form })



def statsSupprimer(request, pacage, annee):
    statistiques = Statistique.objects.all()
    instance = get_object_or_404(Statistique, pacage=pacage, annee=annee)
    instance.delete()

    return redirect('poyosei:statsListe')
  