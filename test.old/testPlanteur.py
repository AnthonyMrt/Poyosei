import sys, os
from django.test import TestCase
from django.core.urlresolvers import reverse
from poyosei.models import *
from poyosei.views import *
from django.db.models.query import QuerySet
from datetime import datetime
from django.shortcuts import get_object_or_404



class CampagneTest(TestCase):
  def setUp(self):
    Planteur.objects.create(pacage='831279456', nom='planteurA', prenom='TestA')
    Planteur.objects.create(pacage='246831759', nom='planteurB', prenom='TestB')
    Planteur.objects.create(pacage='000000000', nom='planteurR', prenom='TestR')
    Campagne.objects.create(pacage='831279456', rid=100, annee=2013)
    Campagne.objects.create(pacage='246831759', rid=50 , annee=2013)
    Campagne.objects.create(pacage='000000000', rid=45 , annee=2013)
    Campagne.objects.create(pacage='831279456', rid=100, annee=2014)
    Campagne.objects.create(pacage='246831759', rid=50 , annee=2014)
    Campagne.objects.create(pacage='000000000', rid=45 , annee=2014)
    Campagne.objects.create(pacage='831279456', rid=100, annee=2019)
    Campagne.objects.create(pacage='246831759', rid=50 , rit=50, annee=2019)
    Campagne.objects.create(pacage='000000000', rid=45, annee=2015)
    Campagne.objects.create(pacage='000000000', rid=45, annee=2019)
    Campagne.objects.create(pacage='831279456', rid=100, annee=2012)
    Campagne.objects.create(pacage='246831759', rid=50 , annee=2012)
    Campagne.objects.create(pacage='000000000', rid=45 , annee=2012) 
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='831279456', pacage_repreneur='246831759', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='temporaire', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='000000000', pacage_repreneur='831279456', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='831279456', pacage_repreneur='000000000', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='246831759', pacage_repreneur='831279456', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='831279456', pacage_repreneur='246831759', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='246831759', pacage_repreneur='831279456', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=False, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='831279456', pacage_repreneur='246831759', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='246831759', pacage_repreneur='831279456', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='831279456', pacage_repreneur='246831759', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=False, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant='246831759', pacage_repreneur='831279456', année_concerne=datetime.now().year,  date_demande=datetime.now(), mouvement_valide=True,type_reference_individuelle_modifie='temporaire', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
    Mouvement.objects.create( type_mouvement='Attribution de Reference Individuelle par la reserve', pacage_cedant='000000000', pacage_repreneur='246831759', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='définitive', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=100, taxe=15)
    Mouvement.objects.create( type_mouvement='Attribution de Reference Individuelle par la reserve', pacage_cedant='000000000', pacage_repreneur='246831759', année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, type_reference_individuelle_modifie='temporaire', date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=50, taxe=15)

  
  def test_annee_derniere_campagne(self):
    PlanteurB = Planteur.objects.get(pacage='831279456')
    annee = PlanteurB.annee
    self.assertEqual(annee, 2019)
  
  def test_rid_derniere_campagne(self):
    PlanteurA = Planteur.objects.get(pacage='000000000')
    rid = PlanteurA.ridDerniereCampagne
    self.assertEqual(rid, 45)

  def test_rid_annee_en_cours(self):
    PlanteurB = Planteur.objects.get(pacage='246831759')
    rid = PlanteurB.ridAnneeEnCours
    self.assertEqual(rid, 121.5)

  def test_rit_annee_en_cours(self):
    PlanteurB = Planteur.objects.get(pacage='246831759')
    rit = PlanteurB.ritAnneeEnCours
    self.assertEqual(rit, -4.5)

  def test_rit_annee_en_cours(self):
    PlanteurB = Planteur.objects.get(pacage='246831759')
    rid = PlanteurB.ridAnneeEnCoursMvtValide
    self.assertEqual(rid, -4.5)

  def test_taxeReserve(self):
    PlanteurB = Planteur.objects.get(pacage='000000000')
    ri = PlanteurB.taxeReserve
    self.assertEqual(ri, 90)

  #def test_ridAnnePrecedente(self):
  #  PlanteurB = Planteur.objects.get('246831759')
  #  test = PlanteurB.ridAnneePrecedente
  #  self.assertListEqual(test, [100])



  def test_createCampagneAuto(self):
    PlanteurE = Planteur.objects.create(pacage='777444111', nom="PlanteurE", prenom='TestE')
    campagneE = Campagne.objects.get(pacage='777444111')
    self.assertTrue(isinstance(campagneE, Campagne))

  
    
  
    
  
  
      
      
      

