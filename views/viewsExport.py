from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
from poyosei.models import *
from poyosei.ressources import PlanteurResource, mouvementResource
from tablib import Dataset
from datetime import datetime
from django.template import loader, Context
from django.db.models import Q
import json
# @csrf_exempt




def planteurExport(request):
    #planteur_resource = PlanteurResource()
    planteurs = Planteur.objects.all()
    listeLigne = []
    #liste_export = []
    toto = "toto"
    CampagneAnnee = Campagne.objects.values_list('annee', flat=True).distinct()
    #listeCampagne = []
    #listeCampagne.append(CampagneAnnee)
    for planteur in planteurs:
        for annee in CampagneAnnee:
            ligne = []
            #try:
            campagnes = get_object_or_404(Campagne, pacage=planteur.pacage, annee=annee)
            statistiques = get_object_or_404(Statistique, pacage=planteur.pacage, annee=annee)
            ligne.append(planteur.planteurExport())
            ligne.append(campagnes.campagneExport(annee))
            ligne.append(statistiques.statistiqueExport(annee))
            #except:
            #ligne.append(planteur.planteurExport())
            listeLigne.append(ligne)


        #toto = list(campagnes)
            #for campagne in campagnes:
                #listeLigne.append(campagne.export)
            
           # for stats in statistiques:




    date = datetime.now().strftime('%Y%m%d-%H%M')
    fields = Planteur._meta.get_fields() + Campagne._meta.get_fields() + Statistique._meta.get_fields()
    csv = render(request, 'rapport/historiqueDesCampagnes.txt', {'ligne':listeLigne, 'fields':fields, 'annee':CampagneAnnee, 'toto':toto})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-campagne.csv"'
    #return render(request, 'my_template_name.txt', {'data': dataset, 'listes':listeP, 'fields':fields})
    return response


    #return response

def mouvementExport(request):
    mouvements = Mouvement.objects.all()
    listeLigne = []
    for mouvement in mouvements:
        ligne = []
        planteurC = get_object_or_404(Planteur, pacage=mouvement.pacage_cedant)
        planteurR = get_object_or_404(Planteur, pacage=mouvement.pacage_repreneur)
        ligne.append(mouvement.mouvementExport())
        ligne.append(planteurC.planteurExport())
        ligne.append(planteurR.planteurExport())
        listeLigne.append(ligne)
    date = datetime.now().strftime('%Y%m%d-%H%M')
    fields = Mouvement._meta.get_fields() + Planteur._meta.get_fields() + Planteur._meta.get_fields()

    csv = render(request, 'rapport/rapportMouvement.txt', {'ligne':listeLigne, 'fields':fields})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-mouvements.csv"'

    return response


def planteurExport2(request, pacage):
    listeLigne = []
    planteur = get_object_or_404(Planteur, pacage=pacage)
    CampagneAnnee = Campagne.objects.values_list('annee', flat=True).distinct()
    for annee in CampagneAnnee:
        ligne = []
        campagnes = get_object_or_404(Campagne, pacage=planteur.pacage, annee=annee)
        statistiques = get_object_or_404(Statistique, pacage=planteur.pacage, annee=annee)
        ligne.append(planteur.planteurExport())
        ligne.append(campagnes.campagneExport(annee))
        ligne.append(statistiques.statistiqueExport(annee))
        #except:
        #ligne.append(planteur.planteurExport())
        listeLigne.append(ligne)


        #toto = list(campagnes)
            #for campagne in campagnes:
                #listeLigne.append(campagne.export)
            
           # for stats in statistiques:

    date = datetime.now().strftime('%Y%m%d-%H%M')
    fields = Planteur._meta.get_fields() + Campagne._meta.get_fields() + Statistique._meta.get_fields()
    csv = render(request, 'rapport/rapportPlanteur.txt', {'ligne':listeLigne, 'fields':fields})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-campagneplanteurs.csv"'

    #return render(request, 'my_template_name.txt', {'data': dataset, 'listes':listeP, 'fields':fields})
    return response


def mouvementExport2(request, pacage):
    listeLigne = []
    mouvements = Mouvement.objects.filter(Q(pacage_cedant=pacage) | Q(pacage_repreneur=pacage))
    for mouvement in mouvements:
        ligne = []
        planteurC = get_object_or_404(Planteur, pacage=mouvement.pacage_cedant)
        planteurR = get_object_or_404(Planteur, pacage=mouvement.pacage_repreneur)
        ligne.append(mouvement.mouvementExport())
        ligne.append(planteurC.planteurExport())
        ligne.append(planteurR.planteurExport())
        listeLigne.append(ligne)
    date = datetime.now().strftime('%Y%m%d-%H%M')
    fields = Mouvement._meta.get_fields() + Planteur._meta.get_fields() + Planteur._meta.get_fields()

    csv = render(request, 'rapport/rapportMouvementDuPlanteur.txt', {'ligne':listeLigne, 'fields':fields})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-mouvements.csv"'

    return response

    

def campagneEnCoursExport(request, pacage):
    listeLigne = []
    planteur = get_object_or_404(Planteur, pacage=pacage)
    CampagneAnnee = Campagne.objects.values_list('annee', flat=True).last()
    ligne = []
    ligne.append(planteur.planteurExport())
    RID = planteur.ridAnneeEnCours
    RIT = planteur.ritAnneeEnCours
    RI = planteur.riTotale
    listeLigne.append(ligne)
    date = datetime.now().strftime('%Y%m%d-%H%M')
    header = ['RI définitive', 'RI temporaire', 'RI Totale']
    fields = Planteur._meta.get_fields()
    csv = render(request, 'rapport/rapportCampagneEnCours.txt', {'ligne':listeLigne, 'test':header, 'RID':RID, 'RIT':RIT, 'RI':RI, 'fields':fields})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-campagneEnCours.csv"'

    return response



def rapportODEADOM(request):
    planteurs = Planteur.objects.all()
    listeLigne = []
    toto = "toto"
    CampagneAnnee = Campagne.objects.values_list('annee', flat=True).distinct()
    for planteur in planteurs:
        for annee in CampagneAnnee:
            ligne = []
            #try:
            campagnes = get_object_or_404(Campagne, pacage=planteur.pacage, annee=annee)
            statistiques = get_object_or_404(Statistique, pacage=planteur.pacage, annee=annee)
            tonnage = get_object_or_404(reconstitutionTonnage, pacage=planteur.pacage, annee=annee)
            ligne.append(planteur.planteurExport())
            ligne.append(campagnes.campagneExport(annee))
            ligne.append(statistiques.statistiqueExport(annee))
            ligne.append(tonnage.tonnageExport(annee))
            prodComTotale = planteur.prodCommercialeTotale(annee)
            
            #except:
            #ligne.append(planteur.planteurExport())
            listeLigne.append(ligne)


            
    date = datetime.now().strftime('%Y%m%d-%H%M')
    fields = Planteur._meta.get_fields() + Campagne._meta.get_fields() + Statistique._meta.get_fields() + reconstitutionTonnage._meta.get_fields()
    header = ['ProdCommercialeTotale']
    csv = render(request, 'my_template_name.txt', {'ligne':listeLigne, 'fields':fields, 'annee':CampagneAnnee, 'total':prodComTotale, 'header':header, 'toto':toto})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-poyosei.csv"'

    #return render(request, 'my_template_name.txt', {'data': dataset, 'listes':listeP, 'fields':fields})
    return response

def rapportODEADOMAnneeEnCours(request):
    planteurs = Planteur.objects.all()
    listeLigne = []
    CampagneAnnee = Campagne.objects.values_list('annee', flat=True).last()
    annee = int(CampagneAnnee)
    for planteur in planteurs:
        ligne = []
        #try:
        campagnes = get_object_or_404(Campagne, pacage=planteur.pacage, annee=annee)
        statistiques = get_object_or_404(Statistique, pacage=planteur.pacage, annee=annee)
        tonnage = get_object_or_404(reconstitutionTonnage, pacage=planteur.pacage, annee=annee)
        ligne.append(planteur.planteurExport())
        ligne.append(campagnes.campagneExport(annee))
        ligne.append(statistiques.statistiqueExport(annee))
        ligne.append(tonnage.tonnageExport(annee))
        prodComTotale = planteur.prodCommercialeTotale(annee)
        
        #except:
        #ligne.append(planteur.planteurExport())
        listeLigne.append(ligne)


            
    date = datetime.now().strftime('%Y%m%d-%H%M')
    fields = Planteur._meta.get_fields() + Campagne._meta.get_fields() + Statistique._meta.get_fields() + reconstitutionTonnage._meta.get_fields()
    header = ['ProdCommercialeTotale']
    csv = render(request, 'my_template_name.txt', {'ligne':listeLigne, 'fields':fields, 'annee':CampagneAnnee, 'total':prodComTotale, 'header':header})
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="' + str(date) +'-poyosei.csv"'

    #return render(request, 'my_template_name.txt', {'data': dataset, 'listes':listeP, 'fields':fields})
    return response




