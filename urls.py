from django.conf.urls import url
from . import views
from poyosei.views import *
app_name = 'poyosei'

urlpatterns = [
    # Static
    url(r'^$', views.index, name='index'),

    # Editer -> Modification
    # Fiche -> Visualisation

    # Planteur

    # url(r'planteur/rid/(?P<pacage>[0-9]+)/$',                                                                     views.planteurRID,                    name='planteurRID'),
    url(r'planteur/ajouter/$', views.planteurAjouter, name='planteurAjouter'),
    url(r'planteur/editer/(?P<pacage>[0-9]+)/$',
        views.planteurEditer, name='planteurEditer'),
    url(r'planteur/export/$', views.planteurExport, name='planteurExport'),
    url(r'planteur/fiche/(?P<pacage>[0-9]+)/$',
        views.planteurFiche,                  name='planteurFiche'),
    url(r'planteur/historique/$',
        views.planteurHistorique,             name='planteurHistorique'),
    url(r'planteur/liste/$', views.planteurListe, name='planteurListe'),
    url(r'planteur/supprimer/(?P<pacage>[0-9]+)/$',
        views.planteurSupprimer,              name='planteurSupprimer'),

    # Relation
    url(r'relation/ajout/(?P<pacage>[0-9]+)/$',
        views.planteurAjoutRelation,          name='planteurAjoutRelation'),

    # Mouvement
    url(r'mouvement/ajouter/$',
        views.mouvementAjouter,               name='mouvementAjouter'),
    url(r'mouvement/editer/(?P<pacage_cedant>[0-9]+)/(?P<pacage_repreneur>[0-9]+)/(?P<id>[0-9]+)/$',
        views.mouvementEditer,                name='mouvementEditer'),
    url(r'mouvement/export/$',
        views.mouvementExport,                name='mouvementExport'),
    url(r'mouvement/fiche/(?P<pacage_cedant>[0-9]+)/(?P<pacage_repreneur>[0-9]+)/(?P<id>[0-9]+)/$',
        views.mouvementFiche,                 name="mouvementFiche"),
    url(r'mouvement/liste/$',
        views.mouvementListe,                 name='mouvementListe'),
    url(r'mouvement/supprimer/(?P<pacage_cedant>[0-9]+)/(?P<pacage_repreneur>[0-9]+)/(?P<id>[0-9]+)/$',
        views.mouvementSupprimer,             name='mouvementSupprimer'),
    url(r'mouvement/historique/$',
        views.mouvementHistorique,            name='mouvementHistorique'),

    # Campagne
    url(r'campagne/liste/$',
        views.campagneListe,                  name='campagneListe'),
    url(r'campagne/ajouter/$',
        views.campagneAjouter,                name='campagneAjouter'),
    url(r'campagne/editer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.campagneEditer,                 name='campagneEditer'),
    url(r'campagne/supprimer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/(?P<id>[0-9]+)/$',
        views.campagneSupprimer,              name='campagneSupprimer'),
    url(r'campagne/fiche/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.campagneFiche,                  name="campagneFiche"),

    # ProductionCommerciale
    url(r'ProdCommerciale/liste/$',
        views.prodCommercialeListe,           name='prodCommercialeListe'),
    url(r'ProdCommerciale/ajouter/$',
        views.prodCommercialeAjouter,         name='prodCommercialeAjouter'),
    url(r'ProdCommerciale/editer/(?P<pacage>[0-9]+)/(?P<année>[0-9]+)/$',
        views.prodCommercialeEditer,          name='prodCommercialeEditer'),
    url(r'ProdCommerciale/fiche/(?P<pacage>[0-9]+)/(?P<année>[0-9]+)/$',
        views.prodCommercialeFiche,           name='prodCommercialeFiche'),
    url(r'ProdCommerciale/supprimer/(?P<pacage>[0-9]+)/(?P<année>[0-9]+)/$',
        views.prodCommercialeSupprimer,       name='prodCommercialeSupprimer'),


    # Statistiques
    url(r'^statistique/liste/$',
        views.statsListe,                     name='statsListe'),
    url(r'^statistique/ajouter/$',
        views.statsAjouter,                   name='statsAjouter'),
    url(r'statistique/editer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.statsEditer,                    name='statsEditer'),
    url(r'statistique/fiche/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.statsFiche,                     name='statsFiche'),
    url(r'statistique/supprimer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.statsSupprimer,                 name='statsSupprimer'),


    # Rapport
    url(r'^rapport/$',
        views.rapport,                        name='rapport'),
    url(r'^rapport/editer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.statsEditer,                    name='statsEditer'),
    url(r'^rapport/fiche/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.statsFiche,                     name='statsFiche'),
    url(r'rapoport/rapportCampagneEnCours/(?P<pacage>[0-9]+)/$',
        views.campagneEnCoursExport,          name='campagneEnCoursExport'),
    url(r'rapport/rapportMouvementDuPlanteur/(?P<pacage>[0-9]+)/$',
        views.mouvementExport2,               name='mouvementExport2'),
    url(r'my_template_name/(?P<pacage>[0-9]+)/$',
        views.planteurExport2,                name='planteurExport2'),
    url(r'rapport/rapportODEADOM/$',
        views.rapportODEADOM,                 name='rapportODEADOM'),
    url(r'rapport/rapportAnnuelODEADOM/$',
        views.rapportODEADOMAnneeEnCours,     name='rapportODEADOMAnneeEnCours'),

    # Opération
    url(r'^operation/$',
        views.operation,                      name='operation'),

    # URL test ajax
    # url(r'^ajax_query/$',                                                                                         views.ajax_query,                     name='ajax_query'),
    # url(r'^ajax/planteur/$',                                                                                      views.searchPlanteur,                 name='searchPlanteur'),

    # Créer nouveau Mouvement
    url(r'^typeMouvement/ajouter/$',
        views.AjouterTypeMouvement,            name='AjouterTypeMouvement'),

    # reconstitutionTonnage
    url(r'^reconstitutionTonnage/liste/$',
        views.tonnageListe,                   name='tonnageListe'),
    url(r'^reconstitutionTonnage/ajouter/$',
        views.tonnageAjouter,                 name='tonnageAjouter'),
    url(r'reconstitutionTonnage/editer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.tonnageEditer,                  name='tonnageEditer'),
    url(r'reconstitutionTonnage/fiche/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.tonnageFiche,                   name='tonnageFiche'),
    url(r'reconstitutionTonnage/supprimer/(?P<pacage>[0-9]+)/(?P<annee>[0-9]+)/$',
        views.tonnageSupprimer,               name='tonnageSupprimer'),

]
