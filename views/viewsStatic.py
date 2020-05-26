from django.db.models import Avg, Sum
from django.shortcuts import render
from poyosei.models import *

def home(request):
    return render(request, 'pages/home.html')

def index(request):
    planteurs = Planteur.objects.all()
    mouvements = Mouvement.objects.all()
    campagne = Campagne.objects.all()
    c = Campagne.objects.order_by('annee').last()
    moyenne = Mouvement.objects.all().aggregate(Avg('quantite_reference_individuelle_accorde'))['quantite_reference_individuelle_accorde__avg'] or 0.00
    total = Mouvement.objects.all().aggregate(Sum('quantite_reference_individuelle_accorde'))['quantite_reference_individuelle_accorde__sum'] or 0.00
    Cannee = int(c.annee)

    return render(request, 'index.html', {'planteurs': planteurs, 'mouvements': mouvements, 'campagne': campagne, 'moyenne':moyenne, 'total':total, 'Cannee':Cannee })

