from django.db import models
from decimal import Decimal
# from project import settings
# import datetime



class reconstitutionTonnage(models.Model):
  pacage                        = models.CharField(max_length=9)
  annee                         = models.CharField(max_length=4)
  reconstitution_tonnage        = models.DecimalField(max_digits=9, decimal_places=0, default=Decimal('0'))
  justification                 = models.TextField()

  class Meta:
    unique_together = ('pacage', 'annee',)

  def __str__(self):
    return self.pacage

  def tonnageExport(self, annee):
    """Fonction qui récupère les noms des champs de la table planteur"""
    Model = reconstitutionTonnage

    line = Model.objects.get(pacage=self.pacage, annee=annee)
    headers = []
    for field in Model._meta.get_fields():
        headers.append(field.name)
    row = []
    for field in headers:
        if field in headers:
            if not Model._meta.get_field(field).is_relation:
                val = getattr(line, field)
                row.append(str(val))

    return row

