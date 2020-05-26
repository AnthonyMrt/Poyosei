from django.conf import settings
from django.db.models import Sum
from django.shortcuts import render
from poyosei.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def operation(request):
  continuer = 'init'
  mouvements = ""
  planteurs = Planteur.objects.all()

  for p in planteurs:
    query = Campagne.objects.filter(pacage=p.pacage)
    camp = Campagne.objects.order_by('annee').last()
    annee = camp.annee

  total = Mouvement.objects.all().filter(année_concerne=annee).aggregate(Sum('quantite_reference_individuelle_accorde'))['quantite_reference_individuelle_accorde__sum'] or 0.00
  totalMouv = Mouvement.objects.all().filter(année_concerne=annee)
  mouvement = Mouvement.objects.filter(mouvement_valide=False)
  nbrM = mouvement.count
  keyword = request.POST.get("order", "")

  annee = Campagne.CampagneEnCours()
  newAnnee = annee + 1

  if request.method == 'POST':
    for t in totalMouv:
      taxin = t.ridReserve 
    for p in planteurs:
      if p.pacage == '000000000':
        total = float(p.ridAnneeEnCours) + taxin
        riTemp = p.ritAnneeEnCours
        Campagne.objects.create(pacage=p.pacage, annee=newAnnee, rid=p.taxeReserve, rit=riTemp, ri_Total=p.riTotale)
      else :
        ridP = p.ridAnneeP
        ritP = p.ritAnneeP
        Campagne.objects.create(pacage=p.pacage, annee=newAnnee, rid=ridP, rit=ritP, ri_Total=p.riTotale)
     


        
      




  return render(request, 'operation/index.html', { 'continuer':continuer, 'annee':annee, 'mouvements':mouvements, 'mouvement':mouvement, "active_tab": "operation", 'total':total, 'totalMouv':totalMouv, 'nbrM':nbrM})

  

