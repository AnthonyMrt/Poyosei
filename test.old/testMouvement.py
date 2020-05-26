import sys, os
from django.test import TestCase
from django.core.urlresolvers import reverse
from poyosei.models import *
from poyosei.views import *
from django.db.models.query import QuerySet
from datetime import datetime
from django.shortcuts import get_object_or_404



class mouvementTest(TestCase):
  def setUp(self):
    Planteur.objects.create(pacage='831279456', nom='planteurA', prenom='TestA')
    Planteur.objects.create(pacage='246831759', nom='planteurB', prenom='TestB')
    Planteur.objects.create(pacage='000000000', nom='planteurC', prenom='TestC')
    Campagne.objects.create(pacage='831279456', rid=100, annee=2013)
    Campagne.objects.create(pacage='246831759', rid=50 , annee=2013)
    Campagne.objects.create(pacage='000000000', rid=45 , annee=2013)
    Campagne.objects.create(pacage='831279456', rid=100, annee=2014)
    Campagne.objects.create(pacage='246831759', rid=50 , annee=2014)
    Campagne.objects.create(pacage='000000000', rid=45 , annee=2014)
    Campagne.objects.create(pacage='831279456', rid=1000, annee=2019)
    Campagne.objects.create(pacage='246831759', rid=50 , rit=50, annee=2019, production_commerciale_totale=30)
    Campagne.objects.create(pacage='000000000', rid=1000 , annee=2019)
    Campagne.objects.create(pacage='831279456', rid=100, annee=2012)
    Campagne.objects.create(pacage='246831759', rid=50 , annee=2012)
    Campagne.objects.create(pacage='000000000', rid=45 , annee=2012)
  def test_transfert_sans_foncier(self):
      mvt1 = Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle sans foncier', pacage_cedant=831279456, pacage_repreneur=246831759, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30, taxe=15)
      mvt = Mouvement.objects.get(pk=mvt1.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -30)
      self.assertEqual(obtenue, 25.5)
      self.assertEqual(taxe, 4.5)

  def test_cession_volontaire_définitive(self):
      mvt2 = Mouvement.objects.create( type_mouvement='Cession volontaire définitive', pacage_cedant=831279456, pacage_repreneur=246831759, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -30)
      self.assertEqual(obtenue, 30)
      self.assertEqual(taxe, 0.0)

  def test_cession_volontaire_temporaire(self):
      mvt2 = Mouvement.objects.create( type_mouvement='Cession volontaire temporaire', pacage_cedant=831279456, pacage_repreneur=246831759, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -30)
      self.assertEqual(obtenue, 30)
      self.assertEqual(taxe, 0.0)

  def test_Cession_activité_sans_repreneur(self):
      mvt2 = Mouvement.objects.create( type_mouvement='Cessation d’activite sans repreneur', pacage_cedant=246831759, pacage_repreneur=000000000, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -30)
      self.assertEqual(obtenue, 30)
      self.assertEqual(taxe, 0.0)

  def test_Transfert_de_Référence_individuelle_avec_foncier(self):
      mvt2 = Mouvement.objects.create( type_mouvement='Transfert de Référence Individuelle avec cession partielle de foncier', pacage_cedant=246831759, pacage_repreneur=831279456, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=30)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -30)
      self.assertEqual(obtenue, 30)
      self.assertEqual(taxe, 0.0)

  def test_Transfert_total_exploitation(self):
      mvt2 = Mouvement.objects.create( type_mouvement='transfert total d\'une exploitation', pacage_cedant=246831759, pacage_repreneur=831279456, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=1000)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -1000)
      self.assertEqual(obtenue, 1000)
      self.assertEqual(taxe, 0.0)

  def test_Attribution_de_reférence_individuelle_par_la_reserve(self):
      mvt2 = Mouvement.objects.create( type_mouvement='Attribution de Reference Individuelle par la reserve', pacage_cedant=000000000, pacage_repreneur=831279456, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=50)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -50)
      self.assertEqual(obtenue, 50)
      self.assertEqual(taxe, 0.0)

  def test_Reprise_administrative(self):
      mvt2 = Mouvement.objects.create( type_mouvement='Reprise administrative', pacage_cedant=246831759, pacage_repreneur=000000000, année_concerne=datetime.now().year, date_demande=datetime.now(), mouvement_valide=True, date_COSDA_Valide=datetime.now(), quantite_reference_individuelle_accorde=50)  
      mvt = Mouvement.objects.get(pk=mvt2.pk)
      ceder = mvt.ridCedant
      obtenue = mvt.ridRepreneur
      taxe = mvt.ridReserve

      self.assertEqual(ceder, -10)
      self.assertEqual(obtenue, 10)
      self.assertEqual(taxe, 0.0)




      


      

  



