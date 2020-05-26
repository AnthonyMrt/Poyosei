from django.shortcuts import render, redirect
# from django.views import View
# from django.views.generic.edit import UpdateView
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
# from poyosei.ressources import PlanteurResource, mouvementResource
# from tablib import Dataset
# import json

# @csrf_exempt

def planteurAjoutRelation(request, pacage):
    form = RelationForm(initial={'pacageA':pacage})
    relations = Relation.objects.filter(pacageA=pacage)

    if request.method == 'POST':
        form = RelationForm(request.POST, initial={'pacageA':pacage})
        if form.is_valid():
            form.save()
            return redirect('poyosei:planteurEditer', pacage=pacage)

    return render(request, 'relation/ajout.html', {"active_tab": "operation", 'form':form, 'relations':relations})


