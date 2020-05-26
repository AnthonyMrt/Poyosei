from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from poyosei.forms import *
from poyosei.models import *



def planteurListe(request):
    planteurs = Planteur.objects.all()
    #active_tab = 'planteur'

    return render(request, 'planteur/liste.html', {'active_tab': 'planteur', 'planteurs': planteurs})


def planteurAjouter(request):
    #Controlleur pour ajouter un planteur
    planteurs = Planteur.objects.all()

    if request.method == 'POST':
        form = PlanteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poyosei:planteurListe')
    else:
        form = PlanteurForm()

        return render(request, 'planteur/ajouter.html', {'active_tab': 'planteur', 'active_tabP': 'ajout', 'form': form, 'planteurs': planteurs})

def planteurEditer(request, pacage):
    #Controlleur pour editer un planteur
    planteurs = Planteur.objects.all()
    instance = get_object_or_404(Planteur, pacage=pacage)
    form = PlanteurForm(request.POST or None, instance=instance)
    mouvements = Mouvement.objects.filter(Q(pacage_cedant=pacage) | Q(pacage_repreneur=pacage))
    relations =  Relation.objects.filter(pacageA=pacage)
    reverse = instance.relation_set.all()
    qry = Planteur.objects.filter(pacage__in=[r for r in reverse])
    statistique = Statistique.objects.filter(pacage=pacage)
    prodCommerciale = ProductionCommerciale.objects.all()

    if form.is_valid():
        planteur = form.save(commit=False)
        planteur.save()

    return render(request, 'planteur/editer.html', {'qry':qry, 'form': form, 'reverse': reverse, 'relations': relations, 'active_tab': 'planteur', 'mouvements':mouvements, 'planteurs': planteurs, 'instance': instance, 'statistique':statistique, 'prodCommerciale':prodCommerciale})

def planteurSupprimer(request, pacage):
    #Controlleur pour supprimer un planteur
    planteurs = Planteur.objects.all()
    query = get_object_or_404(Planteur, pacage=pacage)
    query.delete()

    return redirect('poyosei:planteurListe')


def planteurFiche(request, pacage):
    #Controlleur pour visualiser un planteur
    planteurs = Planteur.objects.all()
    instance = get_object_or_404(Planteur, pacage=pacage)
    form = PlanteurForm(request.POST or None, instance=instance)
    mouvements = Mouvement.objects.filter(Q(pacage_cedant=pacage) | Q(pacage_repreneur=pacage))
    relations =  Relation.objects.filter(pacageA=pacage)
    statistiques = Statistique.objects.all()
    prodCommerciale = ProductionCommerciale.objects.all()

    if form.is_valid():
        planteur = form.save(commit=False)
        planteur.save()

    return render(request, 'planteur/fiche.html', {'form': form, 'active_tab': 'planteur', 'planteurs': planteurs, 'mouvements':mouvements, 'relations':relations, 'instance': instance, 'statistique':statistiques, 'prodCommerciale':prodCommerciale })

def searchPlanteur(request):
    if request.method == 'POST':
        form = PacageForm(request.POST)
        planteurs = ""
        if form.is_valid():
            pacPlan = form.cleaned_data
            planteurSearch = pacPlan['planteurSearch']
            value = request.POST['planteurSearch']
            planteurs = Planteur.objects.filter(pacage__contains=value)

    return render(request, 'poyosei/ajax/ajax.html', {'planteurs' : planteurs})


# def ajax_query(request):
    # form = PacageForm()
    # if request.method == 'POST':
        # form = PacageForm(request.POST)
        # if form.is_valid():
            # pacPlan = form.cleaned_data
            # planteurSearch =  pacPlan['planteurSearch']
            # value = request.POST['planteurSearch']
            # planteurs = Planteur.objects.objects.filter(pacage__contains=value)
            # return HttpResponseRedirect('ajax_query.html', {'planteurs': planteurs})

    # else:
        # form = PacageForm()

    # args = {'form': form}
    # return render(request, 'ajax_query.html', { 'form': form})

def planteurRID(request, pacage):
    instance = Planteur.objects.get(pacage=pacage)
    test = instance.ridAnneeEnCours

    return render(request, 'planteur/rid.html', {'test': test})


def planteurHistorique(request):
    """Controlleur pour l'historique"""
    historique = Planteur.history.all()

    return render (request, 'planteur/historique.html', {'historique':historique} )