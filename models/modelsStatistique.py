from django.db import models
from decimal import Decimal
# from project import settings
# import datetime



class Statistique(models.Model):
  pacage                                = models.CharField(max_length=9, default='')
  annee                                 = models.CharField(max_length=4)
  surface_banane                        = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
  surface_jachere                       = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
  surface_autre                         = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
  surface_totale_utile                  = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
  surface_totale_exploitation           = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
  rendement                             = models.DecimalField(max_digits=9, decimal_places=0, default=Decimal('0'))
  production_exporte                    = models.DecimalField(max_digits=9, decimal_places=0, default=Decimal('0'))
  production_locale                     = models.DecimalField(max_digits=9, decimal_places=0, default=Decimal('0'))
  information_diverse                   = models.TextField(blank=True)
  surface_propriete                     = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
  surface_location                      = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
  commentaire                           = models.TextField(blank=True)


  class Meta:
      ordering = ['pacage']
      unique_together = ('pacage', 'annee',)


  def __str__(self):
    return self.pacage

  
  def prodCommercialeTotale(self):
      """Fonction qui calcule la production production totale d'un planteur pour la campagne en cours"""
      CampagneAnnee = Campagne.objects.values_list('annee', flat=True).last()
      for annee in CampagneAnnee:
          tonnageReconstitué = reconstitutionTonnage.objects.get(pacage=self.pacage, annee=annee)
      
      total = self.production_exporte + self.production_locale + tonnageReconstitué.reconstitution_tonnage

      return total



  
  def statistiqueExport(self, annee):
      """Fonction qui recupère les noms de champs de la table statistique pour les transmettres aux rapport de type CSV"""
      Model = Statistique

      line = Model.objects.get(pacage=self.pacage, annee=annee)
      headers = []
      for field in Model._meta.get_fields():
          headers.append(field.name)
      row = []
      for field in headers:
          if field in headers:
              val = getattr(line, field)
              row.append(str(val))

      return row