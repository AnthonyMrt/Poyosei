# from django.contrib import messages
# from django.contrib.humanize.templatetags.humanize import intcomma
# from django.db.models import Q
# from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
# from django.views import View
# from django.views.generic import ListView
from poyosei.forms import *
from poyosei.models import *
# from tablib import Dataset
# import json

# @csrf_exempt

def tonnageListe(request):
    tonnages = reconstitutionTonnage.objects.all()
    return render(request, 'reconstitutionTonnage/liste.html', {'active_tab': 'tonnage', 'tonnages': tonnages})


def tonnageAjouter(request):
    tonnages = reconstitutionTonnage.objects.all()
    
    if request.method == 'POST':
        form = TonnageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poyosei:tonnageListe')
    else:
        form = TonnageForm()

    
    return render(request, 'reconstitutionTonnage/ajouter.html', {'active_tab': 'tonnage', 'active_tabP': 'ajout', 'form': form, 'tonnages': tonnages})


def tonnageEditer(request, pacage, annee):
    tonnages = reconstitutionTonnage.objects.all()
    instance = get_object_or_404(reconstitutionTonnage, pacage=pacage, annee=annee)
    form = TonnageForm(request.POST or None, instance=instance)

    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('poyosei:tonnageListe')
    else:
        form = TonnageForm(request.POST or None, instance=instance)

    
    return render(request, 'reconstitutionTonnage/editer.html', {'active_tab': 'tonnage', 'form': form, 'instance':instance, 'tonnages': tonnages})


def tonnageFiche(request, pacage, annee):
    tonnages = reconstitutionTonnage.objects.all()
    instance = get_object_or_404(reconstitutionTonnage, pacage=pacage, annee=annee)
    form = TonnageForm(request.POST or None, instance=instance)
    
    return render(request, 'reconstitutionTonnage/fiche.html', {'active_tab': 'tonnage', 'form': form, 'instance':instance, 'tonnages': tonnages})


def tonnageSupprimer(request, pacage, annee):
    tonnages = reconstitutionTonnage.objects.all()
    instance = get_object_or_404(reconstitutionTonnage, pacage=pacage, annee=annee)
    instance.delete()

    return redirect('poyosei:tonnageListe')



















