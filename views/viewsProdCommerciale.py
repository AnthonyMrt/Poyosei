from django.shortcuts import get_object_or_404, render, redirect
# from django.views import View
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
# from poyosei.ressources import PlanteurResource, mouvementResource
# from tablib import Dataset
# import json

# @csrf_exempt

def prodCommercialeListe(request):
    prodCommerciale = ProductionCommerciale.objects.all()

    return render(request, 'prodCommerciale/liste.html', {'active_tab': 'prodCommerciale', 'prodCommerciale':prodCommerciale})

def prodCommercialeAjouter(request):
    prodCommerciale = ProductionCommerciale.objects.all()
    form = ProdCommercialeForm()

    if request.method == 'POST':
        form = ProdCommercialeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poyosei:prodCommercialeListe')
    else:
        form = ProdCommercialeForm()

    return render(request, 'prodCommerciale/ajouter.html', {'form':form, 'active_tab':'prodCommerciale', 'active_tabM': 'ajout', 'prodCommerciale':prodCommerciale })


def prodCommercialeEditer(request, pacage, année):
    prodCommerciale = ProductionCommerciale.objects.all()
    instance = get_object_or_404(ProductionCommerciale, pacage=pacage, année=année)
    form = ProdCommercialeForm(request.POST or None, instance=instance)

    if form.is_valid():
       form = form.save(commit=False)
       form.save()
       return redirect('poyosei:prodCommercialeListe')
    else:
        form = ProdCommercialeForm(request.POST or None, instance=instance)

    return render(request, 'prodCommerciale/editer.html', {'prodCommerciale':prodCommerciale, 'instance':instance , 'form':form })

def prodCommercialeFiche(request, pacage, année):
    prodCommerciale = ProductionCommerciale.objects.all()
    instance = get_object_or_404(ProductionCommerciale, pacage=pacage, année=année)
    form = ProdCommercialeForm(request.POST or None, instance=instance)

    return render(request, 'prodCommerciale/fiche.html', {'prodCommerciale':prodCommerciale, 'instance':instance , 'form':form })




def prodCommercialeSupprimer(request, pacage, année):
    prodCommerciale = ProductionCommerciale.objects.all()
    instance = get_objects_or_404(ProductionCommerciale, pacage=pacage, année=année)
    instance.delete()

    return redirect('poyosei:prodCommercialeListe')

